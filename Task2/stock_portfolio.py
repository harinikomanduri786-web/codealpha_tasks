stocks = {
    "TCS": 3500,
    "INFY": 1600,
    "RELIANCE": 2800
}

total = 0

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stocks:
        qty = int(input("Enter quantity: "))
        total += stocks[stock] * qty
    else:
        print("Stock not found!")

print("Total Portfolio Value: ₹", total)
input("Press Enter to exit...")