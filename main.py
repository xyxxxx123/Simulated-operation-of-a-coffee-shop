import random
from Drink import Drink
from inventory import Inventory

class BaristaGame:
    def __init__(self):
        self.menu = [
            Drink("Espresso", ["coffee_beans"], 3),
            Drink("Latte", ["coffee_beans", "milk"], 4),
            Drink("Cappuccino", ["coffee_beans", "milk", "foam"], 5),
            Drink("Mocha", ["coffee_beans", "milk", "syrup"], 5),
        ]
        self.inventory = Inventory()
        self.total_revenue = 0
        self.purchase_cost = 0
        self.money = 10
        self.rating = 5


    def play_round(self):
        drink = random.choice(self.menu)
        print(f"\nCustomer order: {drink}")
        check = input("Do you want to check the current inventory (yes/no): ").strip().lower()
        while True:       
            if check == 'yes':
                self.inventory.display()
                break
            elif check == 'no':
                break
            else:
                print("Input invalid! Please answer yes/no!")
                check = input("Do you want to check the current inventory (yes/no): ").strip().lower()

        choice = input("Accept order? (yes/no): ").strip().lower()
        while True:
            if choice == 'yes':
                if self.inventory.has_ingredients(drink.ingredients):
                    self.inventory.use_ingredients(drink.ingredients)
                    self.total_revenue += drink.price
                    print(f"Successfully maked {drink.name}! Gained ${drink.price}!")
                else:
                    self.rating -= 1
                    print("The ingredients were insufficient. Order failed!/n Shop rating -1")
                break
            elif choice == 'no':
                print("Refuse roder.")
                break
            else:
                print("Input invalid! Please answer yes/no!")
                choice = input("Accept order? (yes/no): ").strip().lower()
        self.inventory.display()

    def run_day(self, day_number):
        print(f"\nDay {day_number} start! \n(Current money: ${self.money} | rating:{self.rating}/5)")
        rounds = 5
        for _ in range(rounds):
            self.play_round()
            if self.rating <= 0:
                print("Shop rating is 0! Game failed!")
                return False
        spent = self.inventory.restock_with_budget(self.money)
        self.purchase_cost += spent
        self.money -= spent
        return True

    def run(self):
        print("Welcome to Virtual Barista simulated coffee shop!")
        days = int(input("Please enter the number of days you want to operate: "))
        for day in range(1, days + 1):
            if not self.run_day(day):
                break

        net_income = self.total_revenue - self.purchase_cost
        print("\nFinished!")
        print(f"Total income: ${self.total_revenue}")
        print(f"Ingredients cost: ${self.purchase_cost}")
        print(f"Profit: ${net_income}")
        print(f"Final rating: {self.rating}/5")



if __name__ == "__main__":
    game = BaristaGame()
    game.run()
