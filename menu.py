class Food:
    def __init__(self, id, name, prep_time, complexity, cooking_apparatus):
        self.id = id
        self.name = name
        self.prep_time = prep_time
        self.complexity = complexity
        self.cooking_apparatus = cooking_apparatus

## food items
item_1 = Food(1, "Pasta", 20, 2, "oven")
item_2 = Food(2, "Beef Steak", 32, 3, "oven")
item_3 = Food(3, "Waffles", 8, 1, "stove")
item_4 = Food(4, "Chicken Breast", 28, 2, "stove")
item_5 = Food(5, "Cheeseburger", 12, 1, "oven")
item_6 = Food(6, "Cheesecake", 18, 3, "stove")
item_7 = Food(7, "Pizza", 18, 2, "oven")
item_8 = Food(8, "Pasta", 20, 2, "oven")
item_9 = Food(9, "Salad", 9, 1, None)
item_10 = Food(10, "Pasta", 20, 2, "oven")

## menu
menu = [item_1, item_2, item_3, item_4, item_5, item_6, item_7, item_8, item_9, item_10]