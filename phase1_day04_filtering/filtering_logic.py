# Revenue calculation from paid users only

users = ["Amit", "Pavan", "Riya", "Karthik"]
payment_status = ["paid", "free", "paid", "free"]

price_per_user = 499
total_revenue = 0

for index in range(len(users)):
    if payment_status[index] == "paid":
        total_revenue = total_revenue + price_per_user
        print(f"Added payment from {users[index]}")
    else:
        print(f"Skipped {users[index]} (not paid)")

print(f"Total revenue from paid users: ₹{total_revenue}")

