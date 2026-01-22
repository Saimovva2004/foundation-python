# Modeling a user using a dictionary

user = {
    "name": "Pavan",
    "status": "paid",
    "monthly_spend": 1200
}

if user["status"] == "paid" and user["monthly_spend"] >= 1000:
    user_type = "premium"
else:
    user_type = "regular"

print(f"User: {user['name']}")
print(f"User type: {user_type}")

