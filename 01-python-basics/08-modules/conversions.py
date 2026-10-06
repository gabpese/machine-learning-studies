def convert_to_integer(value):
    try:
        return int(value)

    except (ValueError, TypeError):
        return None


def convert_to_float(value):
    try:
        return float(value)

    except (ValueError, TypeError):
        return None


def main():
    print("===== CONVERSION TESTS =====")

    print(convert_to_integer("Ten"))
    print(convert_to_integer("10.0"))
    print(convert_to_integer("10"))

    print(convert_to_float("Ten"))
    print(convert_to_float("10.0"))
    print(convert_to_float("10"))


if __name__ == "__main__":
    main()
