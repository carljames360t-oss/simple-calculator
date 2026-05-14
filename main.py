# main.py
# Entry point for the Simple Calculator app

from calculator import add, subtract, multiply, divide


def run():
    print("=== Simple Calculator ===")
    print("Operations: add, subtract, multiply, divide")
    print("Type 'quit' to exit")
    print()

    while True:
        operation = input("Choose an operation: ").strip().lower()

        if operation == "quit":
            print("Goodbye!")
            break

        if operation not in ("add", "subtract", "multiply", "divide"):
            print("Invalid operation. Try again.")
            continue

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if operation == "add":
            result = add(a, b)
        elif operation == "subtract":
            result = subtract(a, b)
        elif operation == "multiply":
            result = multiply(a, b)
        elif operation == "divide":
            result = divide(a, b)

        print(f"Result: {result}")
        print()


if __name__ == "__main__":
    run()
