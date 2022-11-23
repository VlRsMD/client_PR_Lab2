import requests
import json
import received_order

def receive_order():
    global stack
    receive = requests.get("http://127.0.0.1:3700/get")
    receive_json = receive.json()
    rec_order = json.loads(receive_json, object_hook=received_order.orderIn)
    ## add received order to stack
    stack.append(rec_order)
    print(receive_json)

print('List of orders received by the client: ')
receive_order()