# Discount calculation using step-by-step logic

user_name = input("Enter user name: ")
is_paid = input("Is user paid? (yes/no): ")
total_bill = float(input("Enter total bill amount: "))

if is_paid == "yes" and total_bill >= 1000:
    total_bill = total_bill - 100
    print(f"Discount applied for {user_name}.")
else:
    print(f"No discount for {user_name}.")

print(f"Final bill amount: ₹{total_bill}")

