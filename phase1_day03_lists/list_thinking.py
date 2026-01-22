# Calculating total revenue from multiple users

users = ["Amit", "Pavan", "Riya", "Karthik"]
price_per_user = 499

total_revenue = 0

for user in users:
    total_revenue = total_revenue + price_per_user
    print(f"Added payment from {user}")

print(f"Total revenue: ₹{total_revenue}")

