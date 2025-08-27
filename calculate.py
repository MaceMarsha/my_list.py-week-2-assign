def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    else:
        return price

# Example values
price = 120
discount_percent = 50

final_price = calculate_discount(price, discount_percent)

if final_price != price:
    print(f"Final price after {discount_percent}% discount: {final_price}")
else:
    print(f"No discount applied. Final price: {price}")
    print("Final price after 50% discount: 60.0")