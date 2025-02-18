item = input("What item would you like to buy?: ")
price = float(input("what is the price?: "))
quantity = int(input("How many would like to buy?: "))


total = price * quantity
print(f"you have brought {quantity} X {item}/s")
print(f"Your total before tax is${round(total, 2)}")

# add 10% tax to total bill
tax = total/100 * 10

total = tax + total


print(f"Your total is ${round(total, 2)}")
print(f"Your tax is {tax}%")