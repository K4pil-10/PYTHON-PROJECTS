import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator: ")
letter =int(input("How many letter would you like to have in your password?\n"))
# print(letter)
symbol = int(input("How many symbol would you like to have in password?\n"))
# print(symbol)
number = int(input("How many number would you like to have in password?\n"))

password_list = []
for char in range(0, letter):
    password_list.append(random.choice(letters))

for char in range(0, symbol):
    password_list.append(random.choice(symbols))
for char in range(0, number):
    password_list.append(random.choice(numbers))
print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list :
    password+= char
print(f"Your password is: {password}")