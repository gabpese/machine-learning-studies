finish_message = "Validation completed"

age = 22
has_ticket = True
is_blocked = True
is_vip = True

if is_vip and age >= 18 and not is_blocked:
    print("VIP entry allowed")
elif age >= 18 and has_ticket and not is_blocked:
    print("Entry allowed")
else:
    print("Entry denied")

print(finish_message)
