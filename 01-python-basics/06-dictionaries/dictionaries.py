#   NameError  → name/variable does not exist
#   IndexError → index does not exist in a list
#   KeyError   → key does not exist in a dictionary

course = {
    "name": "Machine Learning with Python",
    "duration_months": 12,
    "active": True
}

person = {
    "name": "Ana",
    "age": 29
}

user = {
    "name": "Gabriel",
    "age": 30,
    "active": True
}

product_1 = {
    "name": "Keyboard",
    "price": 150,
    "stock": 8
}

product_2 = {
    "name": "Mouse",
    "price": 80,
    "stock": 0
}

def show_dictionary_items(dictionary):
    for key, value in dictionary.items():
        print(key, value)

def show_dictionary_keys(dictionary):
    for key in dictionary.keys():
        print(key)

def show_dictionary_values(dictionary):
    for value in dictionary.values():
        print(value)

def check_product(product):
    if product.get("stock", 0) > 0:
        print(product["name"], "Available")
    else:
        print(product["name"], "Out of stock")

dictionaries = [course, person, user, product_1, product_2]

for dictionary in dictionaries:
    print("Dictionary items:")
    show_dictionary_items(dictionary)
    print("-----")
    print("Dictionary keys:")
    show_dictionary_keys(dictionary)
    print("-----")
    print("Dictionary values:")
    show_dictionary_values(dictionary)
    print("=====================================")

check_product(product_1)
check_product(product_2)
