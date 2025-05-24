class Drink:
    def __init__(self, name, ingredients, price):
        self.name = name
        self.ingredients = ingredients
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price}"