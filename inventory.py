import copy

class Inventory:
    def __init__(self):
        self.stock = {
            'coffee_beans': 10,
            'milk': 10,
            'foam': 5,
            'syrup': 5
        }

    def has_ingredients(self, ingredients):
        return all(self.stock.get(i, 0) > 0 for i in ingredients)

    def use_ingredients(self, ingredients):
        for i in ingredients:
            self.stock[i] -= 1

    def restock_with_budget(self, money):
        while True:
            print("\nReplenishment time! Current money${}".format(money))
            view = input("Do you want to check the current inventory (yes/no): ").strip().lower()
            while True:
                if view == 'yes':
                    self.display()
                    break
                elif view == 'no':
                    break
                else:
                    print("Input invalid! Please answer yes/no!")
                    view = input("Do you want to check the current inventory (yes/no): ").strip().lower()

            spent = 0
            temp_money = money
            original_stock = copy.deepcopy(self.stock) 
            for item in self.stock:
                if money <= 0:
                    print("You don't have enough money. Replenishment ending.")
                    break
                while True:
                    try:
                        amount = int(input(f"  replenish {item}?(current {self.stock[item]}):"))
                        if amount < 0:
                            raise ValueError("You can't input negative number. ")
                        if amount > money:
                            print(f"You don't have enough money. You can buy {money} {item} at most. Please input again.")
                            continue
                        self.stock[item] += amount
                        money -= amount
                        spent += amount
                        break
                    except ValueError:
                        print("Invalid input! Please input a integer >0.")

            confirm = input(f"\nConfirm cost ${spent}?(yes/no): ").strip().lower()
            if confirm == 'yes':
                print(f"Replenish finished! Cost ${spent}")
                return spent
            else:
                print("Please replenish again. ")
                self.stock = original_stock
                money = temp_money

    def display(self):
        print("\nCurrent inventory:")
        for k, v in self.stock.items():
            print(f"  {k}: {v}")