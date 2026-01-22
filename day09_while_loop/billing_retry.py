# Simulating a payment retry system

max_attempts = 3
attempt = 1

while attempt <= max_attempts:
    print(f"Attempt {attempt}: Trying payment...")
    
    payment_status = input("Was payment successful? (yes/no): ")
    
    if payment_status == "yes":
        print("Payment successful. Access granted.")
        break
    
    attempt = attempt + 1

if attempt > max_attempts:
    print("Payment failed after maximum retries.")

