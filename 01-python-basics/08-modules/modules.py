import calculator

from conversions import convert_to_integer, convert_to_float
from tools.texts import to_uppercase as uppercase
from tools.texts import to_lowercase


def main():
    print("===== CALCULATOR =====")

    print("Addition:", calculator.add(10, 5))
    print("Subtraction:", calculator.subtract(10, 5))
    print("Multiplication:", calculator.multiply(10, 5))

    division_result = calculator.divide(10, 2)

    if division_result is not None:
        print("Division:", division_result)


    print("\n===== CONVERSIONS =====")

    integer_number = convert_to_integer("25")
    float_number = convert_to_float("10.5")
    invalid_value = convert_to_integer("Python")

    print("Integer:", integer_number)
    print("Float:", float_number)
    print("Invalid conversion:", invalid_value)


    print("\n===== TEXTS =====")

    text = "Machine Learning"

    print(uppercase(text))
    print(to_lowercase(text))


if __name__ == "__main__":
    main()
