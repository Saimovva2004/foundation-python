# Eligibility check for a special discount

user_name = input("Enter user name: ")
is_paid = input("Is user paid? (yes/no): ")
is_sale_period = input("Is it sale period? (yes/no): ")

if is_paid == "yes" and is_sale_period == "yes":
    print(f"{user_name} is eligible for the discount.")
else:
    print(f"{user_name} is NOT eligible for the discount.")

