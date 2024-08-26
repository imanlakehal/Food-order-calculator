total_cost = 0.00
print("Would you like a thin or think crust?")
crust_type = input().lower()
print("Pick a pizza size from 8, 10, 12, 14 or 18 inches")
pizza_size = input().lower()
print("Would you like cheese?")
cheese_type = input().lower()
print("Which pizza type would you like Margherita, Veg, Vegan, Hawaiian or Meat Feast?")
topping_type = input().lower()
print("If you have a voucher code, enter it now. Press enter to skip")
voucher_code = input().lower()
total_cost = 0.00
if crust_type == "thick":
    total_cost = total_cost + 8.00
else:
    total_cost = total_cost + 10.00
if pizza_size == "12" or pizza_size == "14" or pizza_size == "18":
    total_cost = total_cost + 2.00
if cheese_type == "no":
    total_cost = total_cost - 0.50
if topping_type == "veg" or topping_type == "vegan":
    total_cost = total_cost + 1.00
if topping_type == "hawaiian" or topping_type == "meat feast":
    total_cost = total_cost + 2.00
if voucher_code == "FunFriday":
    total_cost = total_cost - 2.00
print(f"Your total cost is: £{total_cost}")