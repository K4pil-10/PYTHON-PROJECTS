print("Welcome to the pizza hub")

pizza_size = input("What size pizza do you want? type S for small M for medium and L for large : ")
pepperoni = input("Do you want pepperoni on pizza? type Y for Yes and N for No: ")
cheese_pizza = input("Do you want to add cheese on pizza? Y for Yes N for No: ")
bill = 0

small_pizza_price = 10
medium_pizza_price = 15
large_pizza_price = 15

cheese_price = 5
pepperoni_price = 5

if pizza_size == "S" :
 bill += small_pizza_price
elif pizza_size == "M" :
 bill +=medium_pizza_price
elif pizza_size == "L" :
 bill += large_pizza_price
else :
 print("Invalid Pizza Size")
if pepperoni == "Y" :
    bill += pepperoni_price

if cheese_pizza == "Y" :
    bill += cheese_price

print(f"You need to pay ${bill}")