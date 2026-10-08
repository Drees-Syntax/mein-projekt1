from __future__ import annotations


def add(x: float, y: float) -> float:
    """Return the sum of two numbers."""
    return x + y


def subtract(x: float, y: float) -> float:
    """Return the difference of two numbers."""
    return x - y


def multiply(x: float, y: float) -> float:
    """Return the product of two numbers."""
    return x * y


def divide(x: float, y: float) -> float:
    """Return the quotient of two numbers."""
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return x / y


def calculate(choice: int, num1: float, num2: float) -> float:
    """Perform the selected operation and return the result."""
    operations = {
        1: add,
        2: subtract,
        3: multiply,
        4: divide,
    }

    if choice not in operations:
        raise ValueError("Invalid operation selected.")

    return operations[choice](num1, num2)


def main() -> None:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    try:
        choice = int(input("Enter choice (1/2/3/4): "))
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = calculate(choice, num1, num2)
        print(f"{num1} {get_symbol(choice)} {num2} = {result}")

    except ValueError as exc:
        print(f"Invalid input: {exc}")
    except ZeroDivisionError as exc:
        print(exc)
    except Exception as exc:
        print(f"An unexpected error occurred: {exc}")


def get_symbol(choice: int) -> str:
    symbols = {
        1: "+",
        2: "-",
        3: "*",
        4: "/",
    }
    if choice not in symbols:
        raise ValueError("Invalid operation selected.")
    return symbols[choice]


if __name__ == "__main__":
    main()
