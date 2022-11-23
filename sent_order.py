class orderOut:
    def __init__(self, order_id, client_id, priority, items, max_wait, generation_time):
        self.order_id = order_id
        self.client_id = client_id
        self.priority = priority
        self.items = items
        self.max_wait = max_wait
        self.generation_time = generation_time