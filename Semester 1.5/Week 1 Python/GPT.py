import datetime

def calculate_payment_date(purchase_date):
    try:
        date_obj = datetime.datetime.strptime(purchase_date, "%Y-%m-%d")
    except ValueError:
        return "Invalid date format. Please use the format YYYY-MM-DD."

    # Check if the day of the month is 25 or greater
    if date_obj.day >= 25:
        payment_date = date_obj.replace(day=1) + datetime.timedelta(days=62)  # Add 62 days for an extra month
    else:
        payment_date = date_obj.replace(day=1) + datetime.timedelta(days=32)  # Add 32 days for the next month

    return payment_date.strftime("%Y-%m-%d")

# Example usage
purchase_date = "2022-02-14"
print("Purchase Date:", purchase_date)
print("Payment Date:", calculate_payment_date(purchase_date))

purchase_date = "2022-02-26"
print("\nPurchase Date:", purchase_date)
print("Payment Date:", calculate_payment_date(purchase_date))