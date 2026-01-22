# Product access rules based on subscription status

user_name = input("Enter user name: ")
subscription_status = input("Enter subscription status (free/paid/expired): ")

if subscription_status == "paid":
    print(f"Full access granted. Welcome, {user_name}!")
elif subscription_status == "free":
    print(f"Limited access granted. Upgrade to unlock more features, {user_name}.")
elif subscription_status == "expired":
    print(f"Subscription expired. Please renew to continue, {user_name}.")
else:
    print("Invalid subscription status. Contact support.")

