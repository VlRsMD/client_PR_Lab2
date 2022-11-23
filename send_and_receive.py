from datetime import datetime
import random
import threading
import requests
import json
import menu
import sent_order
import received_order

stack = []

def send_order():
    order_id = random.randrange(1, 11, 0)
    client_id = random.randrange(1, 11, 0)
    priority = random.randrange(1, 6, 0)
    items = [random.randrange(1, 11, 0), random.randrange(1, 11, 0), random.randrange(1, 11, 0)]
    ## calculating maximum waiting time (5 next lines)
    max = menu.menu[items[0]].prep_time
    for i in range(1, 3):
        if menu.menu[items[i]].prep_time > max:
            max = menu.menu[items[i]].prep_time
    max_wait = max * 1.3
    generation_time = datetime.timestamp(datetime.now())
    new_order = sent_order.orderOut(order_id, client_id, priority, items, max_wait, generation_time)
    order_to_json = json.dumps(new_order.__dict__)
    ## send new order to food ordering service
    requests.post('http://127.0.0.1:3800/client', json = order_to_json)

def threads():
    orders = [threading.Thread(target=send_order) for i in range(10)]
    for order in orders:
        order.start()

def receive_order():
    global stack
    receive = requests.get("http://127.0.0.1:3700/get")
    rec_order = json.loads(receive, object_hook=received_order.orderIn)
    ## add received order to stack
    stack.append(rec_order)
