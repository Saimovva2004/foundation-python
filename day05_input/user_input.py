# Simulating a subscription checkout

customer_name = input("Enter customer name: ")
monthly_price = input("Enter monthly price: ")
active_users = input("Enter number of users: ")

print("\n--- RAW INPUT TYPES ---")
print(type(customer_name))
print(type(monthly_price))
print(type(active_users))

monthly_price = float(monthly_price)
active_users = int(active_users)

revenue = monthly_price * active_users

print("\n--- PROCESSED DATA ---")
print(f"Customer: {customer_name}")
print(f"Monthly price: ₹{monthly_price}")
print(f"Users: {active_users}")
print(f"Total revenue: ₹{revenue}")

