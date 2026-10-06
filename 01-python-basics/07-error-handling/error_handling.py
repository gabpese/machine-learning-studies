# Errors studied:
#
# TypeError         -> operation incompatible with the data type
# NameError         -> name/variable does not exist
# IndexError        -> index does not exist in a sequence
# KeyError          -> key does not exist in a dictionary
# ValueError        -> invalid value for a given operation
# ZeroDivisionError -> attempt to divide by zero
#
# Structure:
#
# try:
#     code that may raise an error
# except ErrorType:
#     error handling
# else:
#     runs if no error occurs
# finally:
#     always runs


# ============================================================
# VALUEERROR AND TYPEERROR
# ============================================================

def convert_to_integer(value):
    try:
        return int(value)

    except ValueError as error:
        print("Invalid value:", error)
        return None

    except TypeError as error:
        print("Invalid type:", error)
        return None


# ============================================================
# INDEXERROR
# ============================================================

def find_item(items, index):
    try:
        return items[index]

    except IndexError as error:
        print("Position does not exist:", error)
        return None


# ============================================================
# KEYERROR
# ============================================================

def find_value(dictionary, key):
    try:
        return dictionary[key]

    except KeyError as error:
        print("Key does not exist:", error)
        return None


# ============================================================
# ZERODIVISIONERROR AND TYPEERROR
# ============================================================

def divide(a, b):
    try:
        return a / b

    except ZeroDivisionError as error:
        print("Cannot divide by zero:", error)
        return None

    except TypeError as error:
        print("Invalid type for division:", error)
        return None


# ============================================================
# TRY / EXCEPT / ELSE / FINALLY
# ============================================================

def validate_number(value):
    try:
        number = int(value)

    except ValueError as error:
        print("Invalid value:", error)

    except TypeError as error:
        print("Invalid type:", error)

    else:
        print("Conversion succeeded.")
        print("Number:", number)

    finally:
        print("Validation completed.")


# ============================================================
# TESTS
# ============================================================

print("----- CONVERSION -----")

result = convert_to_integer("42")

if result is not None:
    print("Result:", result)


print("\n----- INVALID CONVERSION -----")

result = convert_to_integer("Python")

if result is not None:
    print("Result:", result)


print("\n----- LIST -----")

names = ["Ana", "Carlos"]

result = find_item(names, 1)

if result is not None:
    print("Item found:", result)


print("\n----- INVALID INDEX -----")

result = find_item(names, 10)

if result is not None:
    print("Item found:", result)


print("\n----- DICTIONARY -----")

user = {
    "name": "Gabriel",
    "age": 30
}

result = find_value(user, "age")

if result is not None:
    print("Value found:", result)


print("\n----- INVALID KEY -----")

result = find_value(user, "city")

if result is not None:
    print("Value found:", result)


print("\n----- DIVISION -----")

result = divide(100, 2)

if result is not None:
    print("Result:", result)


print("\n----- DIVISION BY ZERO -----")

result = divide(100, 0)

if result is not None:
    print("Result:", result)


print("\n----- ELSE AND FINALLY -----")

validate_number("50")


print("\n----- END OF PROGRAM -----")
