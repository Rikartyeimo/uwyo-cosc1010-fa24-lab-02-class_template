class Pizza:
    def __init__(self, size, sauce="red"):
        self.set_size(size)
        self.sauce = sauce
        self.toppings = ["cheese"]

    def get_size(self):
        return self.size

    def set_size(self, size):
        if size > 10:
            self.size = size
        else:
            self.size = 10

    def get_sauce(self):
        return self.sauce

    def get_toppings(self):
        return self.toppings

    def add_toppings(self, *new_toppings):
        self.toppings.extend(new_toppings)

    def get_amount_of_toppings(self):
        return len(self.toppings)


class Pizzeria:
    price_per_topping = 0.30
    price_per_inch = 0.60

    def __init__(self):
        self.orders = 0
        self.pizzas = []

    def place_order(self):
        size = int(input("Enter the size of the pizza (in inches): "))
        sauce = input("Enter the sauce (default is red): ")
        if not sauce:
            sauce = "red"
        
        toppings = []
        print("Enter toppings (type 'done' when finished):")
        while True:
            topping = input()
            if topping.lower() == 'done':
                break
            toppings.append(topping)
        
        pizza = Pizza(size, sauce)
        pizza.add_toppings(*toppings)
        self.pizzas.append(pizza)
        self.orders += 1

    def get_price(self, pizza):
        return (pizza.get_size() * self.price_per_inch) + (pizza.get_amount_of_toppings() * self.price_per_topping)

    def get_receipt(self, pizza):
        size_price = pizza.get_size() * self.price_per_inch
        toppings_price = pizza.get_amount_of_toppings() * self.price_per_topping
        total_price = size_price + toppings_price

        receipt = (
            f"Receipt:\n"
            f"Sauce: {pizza.get_sauce()}\n"
            f"Size: {pizza.get_size()} inches\n"
            f"Toppings: {', '.join(pizza.get_toppings())}\n"
            f"Price for size: ${size_price:.2f}\n"
            f"Price for toppings: ${toppings_price:.2f}\n"
            f"Total price: ${total_price:.2f}\n"
        )
        print(receipt)

    def get_number_of_orders(self):
        return self.orders


# Main program
pizzeria = Pizzeria()

while True:
    order = input("Do you want to order a pizza? (type 'exit' to quit): ")
    if order.lower() == 'exit':
        break
    pizzeria.place_order()
    pizzeria.get_receipt(pizzeria.pizzas[-1])

print(f"Total number of orders placed: {pizzeria.get_number_of_orders()}")