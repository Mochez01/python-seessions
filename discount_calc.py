## creating afuction to calculate the discount on a product
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    return price

# taking input from the user
price1 = int(input("Enter the price: "))
discount1 = int(input("Enter the discount percentage: "))
final_price1 = calculate_discount(price1, discount1)
print(f"The final price after discount is: {final_price1}")

