from datetime import datetime
import random
import threading
import requests
import json
import menu
import sent_order

stack = []

def send_order():
    id = random.randrange(10)+1
    client_id = random.randrange(10)+1
    priority = random.randrange(5)+1
    items = [random.randrange(10)+1, random.randrange(10)+1, random.randrange(10)+1]
    ## calculating maximum waiting time (5 next lines)
    max = menu.menu[items[0]-1].prep_time
    for i in range(1, 3):
        if menu.menu[items[i]-1].prep_time > max:
            max = menu.menu[items[i]-1].prep_time
    max_wait = max * 1.3
    generation_time = datetime.timestamp(datetime.now())
    new_order = sent_order.orderOut(id, client_id, priority, items, max_wait, generation_time)
    order_to_json = json.dumps(new_order.__dict__)
    ## send new order to food ordering service
    send = requests.post('http://127.0.0.1:3800/client', json = order_to_json)
    ##print(send.json())

def threads():
    orders = [threading.Thread(target=send_order) for i in range(10)]
    for order in orders:
        order.start()

##print('List of orders sent by the client: ')
threads()

