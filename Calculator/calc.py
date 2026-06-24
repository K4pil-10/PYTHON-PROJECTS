from logo import art

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def remainder(num1, num2):
    return num1 % num2


operations = {
    "+" : add,
    "-" : subtract,
    "*": multiply,
    "/": divide,
    "%": remainder,
}

# print(operations["*"](num1=8, num2=2))

def calculator():
    print(art)
    should_continue = True
    num1= float(input("Enter First Number: "))

    while should_continue:
        for symbol in operations:
            print(symbol)
        operations_symbol= input("Pick an operation: ")
        num2= float(input("Enter Second Number: "))
        answer= operations[operations_symbol](num1, num2)
        print(f"{num1} {operations_symbol} {num2} = {answer}")

        choice= input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            num1 = answer
        else:
            should_continue = False
            print("\n" * 20)
            calculator()
calculator()


