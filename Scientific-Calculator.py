def add(a, b):
    total = a + b
    return total

def subtract(a, b):
    total = a - b
    return total

def multiply(a, b):
    total = a * b
    return total

def divide(a, b):
    total = a / b
    return total

def power(a, b):
    total = a ** b
    return total

def square_root(a):
    total = math.sqrt(a)
    return total   
    
def percentage(a, b):
    total = a * b / 100
    return total
    
def sine(a):
    total = math.sin(math.radians(a))
    return total
    
def cosine(a):
    total = math.cos(math.radians(a))
    return total

def tangent(a):
    total = math.tan(math.radians(a))
    return total

def add_to_history(history, operation):
    if len(history) == 5:
        history.pop(0)

    history.append(operation)

def return_to_menu():
    while True:

        option = int(input("Enter 0 to return to the menu:"))

        if option == 0:
            break

def invalid_option():
    print("Error: Invalid option.")
    return_to_menu()


history = []
running = True

import math 

while running:

    # Menu
    print("========================")
    print("   SCIENTIFIC CALCULATOR")
    print("========================")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. percentage")
    print("8. Sine")
    print("9. Cosine")
    print("10.Tangent")
    print("0. History")
    print("11. Exit")
    print("========================")

    option = int(input("Choose an operation: "))

    # Decisions
    if option == 1:

        a = float(input("First number:"))
        b = float(input("Second number:"))

        result = add(a, b)
        print(f"{result:.2f}")
        add_to_history(history, f"{a} + {b} = {result:.2f}")

        return_to_menu()

    elif option == 2:

        a = float(input("First number:"))
        b = float(input("Second number:"))

        result = subtract(a, b)
        print(f"{result:.2f}")
        add_to_history(history, f"{a} - {b} = {result:.2f}")

        return_to_menu()

    elif option == 3:

        a = float(input("First number:"))
        b = float(input("Second number:"))

        result = multiply(a, b)
        print(f"{result:.2f}")
        add_to_history(history, f"{a} * {b} = {result:.2f}")

        return_to_menu()

    elif option == 4:

        a = float(input("First number:"))
        b = float(input("Second number:"))

        try:
            result = divide(a, b)
            print(f"{result:.2f}")
            add_to_history(history, f"{a} / {b} = {result:.2f}")

        except ZeroDivisionError:
            print("Error: Division by zero.")

        return_to_menu()

    elif option == 5:

        a = float(input("First number:"))
        b = float(input("Second number:"))

        result = power(a, b)
        print(f"{result:.2f}")
        add_to_history(history, f"{a} ^ {b} = {result:.2f}")

        return_to_menu()
        
    elif option == 6:

       a = int(input("Insert Number:"))
      
       result = square_root(a)

       print(f"{result:.2f}")

       add_to_history(history, f"√{a} = {result:.2f}")

       return_to_menu()
       
    elif option == 7:

       a = int(input("Insert Number:"))
       b = int(input("Insert Number:"))
      
       result = percentage(a, b)

       print(f"{result:.2f}")

       add_to_history(history, f"{a}% of {b} = {result:.2f}")

       return_to_menu()
       
    elif option == 8:

       a = float(input("Insert Number:"))
      
       result = sine(a)

       print(f"{result:.2f}")

       add_to_history(history, f" sin({a}°) = {result:.2f}")

       return_to_menu()
       
    elif option == 9:

       a = float(input("Insert Number:"))
      
       result = cosine(a)

       print(f"{result:.2f}")

       add_to_history(history, f" cos({a}°) = {result:.2f}")

       return_to_menu()
      
    elif option == 10:

       a = float(input("Insert Number:"))
      
       result = tangent(a)

       print(f"{result:.2f}")

       add_to_history(history, f" tan({a}°) = {result:.2f}")

       return_to_menu()

    elif option == 11:
        running = False
        print("Thank you for testing!")

    elif option == 0:

        in_history = True

        while in_history:

            print("======== HISTORY ========")

            if not history:
                print("No operations performed.")

            else:
                for number, operation in enumerate(history, 1):
                    print(f"{number}. {operation}")

            option = int(input("Enter 0 to return to the main menu:"))

            if option == 0:
                in_history = False

    else:
        print("Error: Invalid option.")
        invalid_option()
