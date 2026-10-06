def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    try:
        return a / b

    except ZeroDivisionError as error:
        print("Cannot divide by zero:", error)
        return None

    except TypeError as error:
        print("Invalid type for division:", error)
        return None


def main():
    print("===== CALCULATOR TESTS =====")

    print("Addition:", add(10, 5))
    print("Subtraction:", subtract(10, 5))
    print("Multiplication:", multiply(10, 5))
    print("Division:", divide(10, 5))

    print("\nDivision by zero test:")
    print(divide(10, 0))


if __name__ == "__main__":
    main()
