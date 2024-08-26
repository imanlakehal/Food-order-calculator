total_cost = 0.00
sugar_tax = 0.50
print("Would you like a Sandwich or Wrap?")
bread_type = input()
print("Do you want that Meat, Vegetarian or Vegan?")
filling_type = input()
print("Extra salad?")
salad_type = input().lower()
print("Extra sauce?")
sauce_type = input().lower()
print("For your dessert, Cookie, Crisps, Fruit or None")
pudding = input()
print("And for your drink, Fizzy drink, Water, Juice or None")
drink = input()
if bread_type != "sandwich":
    total_cost = 2.00
else:
    total_cost = 3.00
if filling_type == "vegetarian" or filling_type == "vegan":
    total_cost = total_cost + 1.00
else:
    total_cost = total_cost + 1.50
if sauce_type == "yes" and salad_type == "yes":
    total_cost = total_cost + 1.0
if pudding == "cookie" and drink == "fizzy drink":
    total_cost = total_cost + sugar_tax
if pudding == "none" or drink == "none":
    total_cost = total_cost - 0.50
print(f"Your total cost is: £{total_cost}")