# Problem-solving example: billing decision

customer_name = input("Enter customer name: ")
monthly_price = float(input("Enter monthly price: "))
payment_status = input("Is payment successful? (yes/no): ")

if payment_status == "yes":
    print(f"Payment received. Access granted to {customer_name}.")
    print(f"Total bill: ₹{monthly_price}")
else:
    print(f"Payment not received. Access denied for {customer_name}.")

