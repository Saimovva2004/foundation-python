# Invoice-style message example

company_name = "FinTrack"
customer_name = "Pavan"
monthly_price = 499
gst_rate = 0.18

gst_amount = monthly_price * gst_rate
final_price = monthly_price + gst_amount

message = (
    f"Hello {customer_name},\n"
    f"Thank you for subscribing to {company_name}.\n"
    f"Base price: ₹{monthly_price}\n"
    f"GST (18%): ₹{gst_amount}\n"
    f"Total payable amount: ₹{final_price}\n"
)

print(message)

