def orders_by_shipment():
    results = resultado
    if results == None: print("Error")
    return list(map(lambda item: item['order_id'], results))


resultado = [{"manufacturing_time": None, "quantity": 1, "item_id": "MLB2143305189", "variation_id": 174472969263,
              "dimensions_source": {"origin": "fulfillment", "id": "MLB2143305189-174472969263"},
              "description": "Capa A03 Core + Película 3d Smsng Lançamento Silicone", "order_id": "2000003967168502",
              "sender_id": 256618785, "dimensions": {"width": 16,
                                                     "length": 18, "weight": 90, "height": 4}},
             {"manufacturing_time": None, "quantity": 1, "item_id": "MLB1755426862", "variation_id": 72248955070,
              "dimensions_source": {"origin": "fulfillment", "id": "MLB1755426862-72248955070"},
              "description": "Película De Vidro 3d P/ iPhone 7/8 Plus Xs Xr 11 Pro Max 12",
              "order_id": "2000003967167496",
              "sender_id": 539320826, "dimensions": {"width": 11, "length": 21, "weight": 20, "height": 2}},
             {"manufacturing_time": None, "quantity": 1, "item_id": "MLB1876623008", "variation_id": 83872614114,
              "dimensions_source": {"origin": "fulfillment", "id": "MLB1876623008-83872614114"},
              "description": "Capa Capinha Silicone Compatível iPhone 7 Plus E 8 Plus", "order_id": "2000003967167498",
              "sender_id": 607470519, "dimensions": {"width": 11, "length": 18, "weight": 40, "height": 2}}]

print(orders_by_shipment())