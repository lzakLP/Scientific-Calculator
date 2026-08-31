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


def add_to_history(history, operation):
    if len(history) == 5:
        history.pop(0)

    history.append(operation)


def return_to_menu():
    while True:

        option = int(input("Enter 0 to return to the menu:"))

        if option == 0:
            break


history = []
running = True

while running:

    # Menu
    print("========================")
    print("   SCIENTIFIC CALCULATOR")
    print("========================")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
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
        return_to_menu()