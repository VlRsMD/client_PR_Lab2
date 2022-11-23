class orderOut:
    def __init__(self, id, client_id, priority, items, max_wait, generation_time):
        self.id = id
        self.client_id = client_id
        self.priority = priority
        self.items = items
        self.max_wait = max_wait
        self.generation_time = generation_time