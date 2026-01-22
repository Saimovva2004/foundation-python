# Subscription pricing example

monthly_price = 499
gst_rate = 0.18
active_users = 120

gst_amount = monthly_price * gst_rate
final_price = monthly_price + gst_amount

monthly_revenue = final_price * active_users

print("Base price:", monthly_price)
print("GST amount:", gst_amount)
print("Final price per user:", final_price)
print("Active users:", active_users)
print("Monthly revenue:", monthly_revenue)

