from app.core.scripting.script_engine import ScriptEngine, ScriptCommandLineConverter
from app.core.scripting.script_output import ScriptOutput, SOL_TYPE, MSG_TYPE, SQUAD
from app.core.scripting.script_error import ScriptError

import json
import sys, os, asyncio, re
from http import HTTPStatus
from urllib.parse import urlencode

SCRIPT_NAME = 'cancelled_order_wms'  # TODO nombre del archivo .py
SCRIPT_VERSION = '1.0.0'
SQUAD_OWNER = SQUAD.FBM_GO  # TODO actualizar
INPUT_FIELDS = ['shipment_id']  # TODO actualizar
PARAMS = ['force_cancelled']  # TODO actualizar


class CancelledOrderWms(ScriptEngine):  # TODO cambiar nombre de clase acorde al script
    def __init__(self, execute: bool, ticket_id: str, session_id: str):
        # self.CLIENT_ID = os.environ.get('SECRET_CLIENT_ID')
        # if self.CLIENT_ID in [None, '']: raise Exception("[REQUIRED] Para poder ejecutar el script, debe crear la variable de entorno [SECRET_CLIENT_ID]. Ejecutar por terminal:\nexport SECRET_CLIENT_ID=\"CLIENT_ID\"")

        super().__init__(execute, ticket_id, session_id, SCRIPT_NAME, SCRIPT_VERSION, SQUAD_OWNER)

    def validate_params(self, script_params: dict) -> dict:
        process_allowed = ['False', 'True']

        self.FORCE_CANCELLED = script_params.get('force_cancelled')

        if self.FORCE_CANCELLED not in process_allowed:  raise ValueError(
            f"[REQUIRED] El parámetro [FORCE_CANCELLED] debe ser igual a {process_allowed}.")
        return script_params

    # TODO
    def validate_record_format(self, record: dict, input_fields: list) -> dict:
        regex_per_field: dict = {
            'shipment_id': '^[4]{1}[0-9]{10}$',
        }
        for index, key in enumerate(input_fields):
            if record.get(key) in [None, '']:                        raise ScriptError(MSG_TYPE.REJECT,
                                                                                       f"El {index + 1}º campo [{key}] es requerido.",
                                                                                       SOL_TYPE.WRONG_INPUT_FORMAT)
            if re.search(regex_per_field[key], record[key]) is None: raise ScriptError(MSG_TYPE.REJECT,
                                                                                       f"El {index + 1}º campo [{key}] no se corresponde con el formato => {regex_per_field[key]}",
                                                                                       SOL_TYPE.WRONG_INPUT_FORMAT)

        return record

    # TODO
    def process_record(self, record: dict) -> ScriptOutput:
        output: ScriptOutput = None

        problems = ['PROBLEM_ID']
        try:
            # item = self.get_item(record['field'])
            order_mkp = self.get_order_mkp(record['shipment_id'])
            self.validate_order(order_mkp, record['shipment_id'])
            self.post_item(self.payload_for_item(record))

            output = ScriptOutput(MSG_TYPE.OK if self.EXECUTE else MSG_TYPE.SIMULATION, "Se procesó exitostamente.",
                                  SOL_TYPE.RESOLVED, problems=problems)
        except ScriptError as e:
            output = e.get_script_output()
        except Exception as e:
            self.LOG.debug(e, exc_info=True)
            raise ScriptError(MSG_TYPE.ACTION,
                              f"Derivar a [{self.SQUAD_OWNER.value}]: Ocurrieron errores en [process_record] => {str(e)}",
                              SOL_TYPE.DERIVED_ERROR_WORKAROUND, derivar_a=self.SQUAD_OWNER, problems=problems)
        output.metric = {'entity_name': 'entity_name',
                         'entity_id': str(record['entity_id'])}  # TODO detallar bien entity_name/entity_id

        return output

    def validate_order(self, order_mkp, order):

        status_mkp = self.validate_order_mkp(order_mkp)

        if status_mkp in [None, '']:
            raise ScriptError(MSG_TYPE.ERROR, f"Orden [{order}] inexistente", SOL_TYPE.OUT_OF_SCOPE)
        else:
            order_wms = self.get_outbound_group(order_mkp['warehouse_id'], order)
        results_validate: list = self.validate_order_wms(order_wms, order_mkp['logistic_type'])

        if results_validate[0] in [None, ''] and results_validate[1] not in [None, '']:
            raise ScriptError(MSG_TYPE.ACTION, f"{results_validate[1]}", SOL_TYPE.OUT_OF_SCOPE)
        elif results_validate[1] in [None, ''] and results_validate[0] not in [None, '']:
            status_wms = results_validate[0]
            self.validate_cancellation(status_mkp, status_wms, order_mkp)
        # raise ScriptError(MSG_TYPE.REJECT, f"[{item}]", SOL_TYPE.OUT_OF_SCOPE)
        # raise ScriptError(MSG_TYPE.REJECT, f"[{item}]", SOL_TYPE.DOES_NOT_REPRODUCE)
        pass

    # Metodo privado para desacoplar tareas del validate_order()
    def validate_order_mkp(self, order_mkp):
        status_mkp = ''
        if order_mkp in [None, '']:
            return None
        else:
            status_mkp = order_mkp['status']
            return status_mkp

    # Metodo privado para desacoplar tareas del validate_order()
    def validate_order_wms(self, order_wms, mkp_logistic_type):
        status_wms = ''
        msg_error = ''
        if order_wms in [None, '']:
            if mkp_logistic_type != 'fullfilment':
                msg_error = f"La orden corresponde a la logistística {mkp_logistic_type}\nSOLUCION: Modificar la CATEGORÍA y REQUEST TYPE del ticket a 'Entidades y Configuraciones >> Envios - Cambios de Estado' Resolver con el procedimiento: https://sites.google.com/mercadolibre.com/gestion-operativa/help-desk/procedimientos-helpdesk/cambio-de-estado-de-env%C3%ADos"
            else:
                msg_error = "SOLUCION: PASAR A GO INFORMANDO QUE LA ORDEN TIENE LOGÍSTICA FULFILLMENT PERO NO EXISTE EN WMS"
        else:
            status_wms = order_wms['status']
        return [status_wms, msg_error]

        # Metodo privado para desacoplar tareas del validate_order()

    def validate_cancellation(self, status_mkp, status_wms, order_mkp):
        msg_info = ''
        if status_mkp == "cancelled":
            if status_wms in ["cancelled", "returned", "unavailable"]:
                msg_info = "SOLUCION: Actualizar ticket a \"No se pudo reproducir\"\nCOMENTARIO: La order ya se encuentra cancelada"
            else:
                msg_info = "SOLUCION: Debe actualizarse la order a 'cancellled' o 'unavailable' en WMS\nCOMENTARIO: Ejecutar con el script https://github.com/mercadolibre/fury_lib-shipping-go/blob/master/Fulfillment/Wms/Orders/scanOrdersWms.groovy"
        elif status_mkp in ["delivered", "shipped", "not_delivered"]:
            if status_wms == "out":
                msg_info = "SOLUCION: RECHAZAR TICKET\nCOMENTARIO: La order se encuentra shipped no podemos cancelar la misma"
            else:
                msg_info = f"SOLUCION: RECHAZAR TICKET\nCOMENTARIO: No se puede cancelar la order \nShipment= {status_mkp}, order != shipped\nEjecutar con el script https://github.com/mercadolibre/fury_lib-shipping-go/blob/master/Fulfillment/Wms/Orders/scanOrdersWms.groovy"
        elif status_wms in ["planning", "pending", "picking", "sorting", "to_group", "grouping", "grouped", "to_pack"]:
            msg_info = f"SOLUCION: RECHAZAR TICKET\nCOMENTARIO: La order no puede cancelarse, se encuentra en status {status_wms}. Solo cancelamos si se encuentra en un estado posterior al packing y algun producto se rompio o perdio.\nEjecutar con el script https://github.com/mercadolibre/fury_lib-shipping-go/blob/master/Fulfillment/Wms/Orders/scanOrdersWms.groovy para intentar destrabarla."
        elif status_wms in ["packed", "to_document", "documented", "to_dispatch", "to_out", "unavailable"]:
            if (self.FORCE_CANCELLED == True):
                pass
        pass

    # Metodo tocado
    def get_order_mkp(self, order_id: str):
        url: str = f"/shipments/{order_id}?caller.scopes=admin&client.id=1360974954364596"
        result = self.get(url)
        if result == None: raise ScriptError(MSG_TYPE.REJECT, f"No se pudo encontrar la order [{order_id}].",
                                             SOL_TYPE.API_ERROR)
        return result.json() if result != None else None

    def get_outbound_group(self, warehouse_id: str, order_id: str):
        url: str = f"/wms/warehouses/{warehouse_id}/outbound/groups/order/{order_id}?client.id=123"
        result = self.get(url)
        if result == None: raise ScriptError(MSG_TYPE.REJECT,
                                             f"No se pudo encontrar el outbound_group de la order [{order_id}].",
                                             SOL_TYPE.API_ERROR)
        return result.json() if result != None else None

    def deletePayment(self, shipment_id, cause):
        # refund = Shipment.refundByShipment(shipment_id, cause)

        ORDER_MKP = self.get_order_mkp(shipment_id)
        if ORDER_MKP['status'] == "cancelled":
            return 200
        else:
            return 0

    ################### Template Scrpit ######################################
    def payload_for_item(self, record: dict):
        payload: json = {"id": record['id']}
        return payload

    def post_item(self, payload: json):
        url: str = f"/internal/uri"
        # x_idempotency_key:str = f"{self.WMS_USER_ID}-{datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')}"
        # headers = {'X-Idempotency-Key':x_idempotency_key}
        result = self.post(url, json=payload)
        return (
            result.json() if self.EXECUTE and result != None and result.status_code != HTTPStatus.NO_CONTENT else None)

    def put_item(self, payload: json):
        url: str = f"/internal/uri"
        result = self.put(url, json=payload)
        return (
            result.json() if self.EXECUTE and result != None and result.status_code != HTTPStatus.NO_CONTENT else None)

    def delete_item(self, item_id: str):
        url: str = f"/uri/{item_id}"
        result = self.delete(url)
        return (
            result.json() if self.EXECUTE and result != None and result.status_code != HTTPStatus.NO_CONTENT else None)


CMD_HELP = '''
usage: python SCRIPT_NAME.py [options] | [configs] | [params]
[options]
    -h --help
    -v --version
[configs]
    -s --session_id value (mandatory) cookie de https://shipping-bo.adminml.com/, requerido si --execute
    -t --ticket_id  value (optinal)   requerido si se envía el parámetro --execute (pudiendo ingresar SIN_TICKET en caso de no tener uno)
    -e --execute          (optinal)   parámetro sin valor, si no está presente => ejecuta en modo simulación
[params]
    -i --input input.csv  (mandatory) archivo sin cabecera que contenga los registros a procesar => INPUT_FIELDS
    --action value        (mandatory) ALTA/BAJA
        --action ALTA
        --action BAJA
    --warehouse_id value  (mandatory) site de meli
        --warehouse_id ARBA01
        --warehouse_id BRSP02
        ...

simulation sample => python path/.../SCRIPT_NAME.py -i scripts/input.csv -t SSHP_ID --action ACTION --warehouse_id WAREHOUSE_ID
execution  sample => python path/.../SCRIPT_NAME.py -e -i scripts/input.csv -t SSHP_ID -s SESSION_ID --action ACTION --warehouse_id WAREHOUSE_ID 
'''.replace("SCRIPT_NAME", SCRIPT_NAME).replace("INPUT_FIELDS", ','.join(
    INPUT_FIELDS))  # TODO documentar bien forma de ejecución (recordar detallar bien el path)

CMD_VERSION = '''
- Version:       SCRIPT_NAME-SCRIPT_VERSION
- Description:   https://mercadolibre.atlassian.net/wiki/spaces/SSHP/pages/SMO_CONFLUENCE_ID
- Responsables:  FBM-GO => Nombre Apellido (análisis) / Nombre Apellido (código)
- Tracer(audit): https://meli.looker.com/dashboards/2481?Process+Name="SCRIPT_NAME"&Created+Time=this+quarter
- Metrics:       https://meli.looker.com/dashboards/2483?Process+Name="SCRIPT_NAME"&Created+Time=this+quarter
'''.replace('SCRIPT_NAME', SCRIPT_NAME).replace('SCRIPT_VERSION',
                                                SCRIPT_VERSION)  # TODO completar Descripción (problems?) y Responsables

if __name__ == '__main__':
    sys.stderr = open(os.devnull,
                      "w")  # suprimir warnings/errors de python que se imprimen por consola (como por ejemplo un timeout de un request)

    try:
        short_params: str = ''  # opcional, puede quedar '' / no se pueden usar => h(help) / v(version) / e(execute) / s(session_id) / t(ticket_id) / i(input)
        short_param_names: dict = {}  # si no utilizaste short_params, esto queda vacío {}
        long_params: tuple = list(map(lambda param: f"{param}=", PARAMS))

        SCRIPT_PARAMS = ScriptCommandLineConverter(sys.argv[1:], short_params, long_params,
                                                   short_param_names).get_script_params()
        if 'help' in SCRIPT_PARAMS:   raise ValueError("Help")
        if 'version' in SCRIPT_PARAMS:   raise Exception(CMD_VERSION)

        EXECUTE = SCRIPT_PARAMS['execute']
        TICKET_ID = SCRIPT_PARAMS['ticket_id']
        SESSION_ID = SCRIPT_PARAMS['session_id']
        RAW_INPUT = open(SCRIPT_PARAMS['input'], 'r').read()

        script = CancelledOrderWms(EXECUTE, TICKET_ID,
                                   SESSION_ID)  # TODO cambiar nombre de clase acorde a la declarada arriba.
        results = asyncio.run(script.execute(SCRIPT_PARAMS, RAW_INPUT, INPUT_FIELDS))
    except (ValueError, KeyError) as e:
        print(f"{str(e)}\n{CMD_HELP}")
    except Exception as e:
        print(f"{str(e)}")