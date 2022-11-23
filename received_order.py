class orderIn:
    def __init__(self, order_id, client_id, restaurant_id, priority, items, max_wait, generation_time, cooking_time, cook):
        self.order_id = order_id
        self.client_id = client_id
        self.restaurant_id = restaurant_id
        self.priority = priority
        self.items = items
        self.max_wait = max_wait
        self.genration_time = generation_time
        self.cooking_time = cooking_time
        self.cook = cook