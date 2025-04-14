def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price

# Prompt user for input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Call the function and get the final price
final_price = calculate_discount(price, discount_percent)

# Print the result
if discount_percent >= 20:
    print(f"The final price after a {discount_percent}% discount is: Ksh.{final_price:.2f}")
else:
    print(f"No discount applied. The price remains: Ksh.{price:.2f}")