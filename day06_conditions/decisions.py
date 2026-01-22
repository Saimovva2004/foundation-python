# Subscription access decision

user_name = input("Enter user name: ")
is_payment_successful = input("Is payment successful? (yes/no): ")

if is_payment_successful == "yes":
    print(f"Access granted. Welcome, {user_name}!")
else:
    print(f"Access denied. Please complete payment, {user_name}.")

