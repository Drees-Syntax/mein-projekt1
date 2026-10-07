# Program make a simple calculator that can add, subtract, multiply and divide using functions

# define functions
def add(x, y):
    """Return the sum of two numbers."""
    return x + y


def subtract(x, y):
    """Return the difference of two numbers."""
    return x - y


def multiply(x, y):
    """Return the product of two numbers."""
    return x * y


def divide(x, y):
    """Return the quotient of two numbers."""
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return x / y


def calculate(choice, num1, num2):
    """Perform the selected operation."""
    operations = {
        1: ("+", add),
        2: ("-", subtract),
        3: ("*", multiply),
        4: ("/", divide),
    }

    if choice not in operations:
        raise ValueError("Invalid operation selected.")

    symbol, func = operations[choice]
    result = func(num1, num2)
    print(f"{num1} {symbol} {num2} = {result}")
    return result


def main():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    try:
        choice = int(input("Enter choice (1/2/3/4): "))
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        calculate(choice, num1, num2)

    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except ZeroDivisionError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
