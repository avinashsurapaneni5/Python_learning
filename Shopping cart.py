item = input("What item would you like to buy?: ")
price = float(input("what is the price?: "))
quantity = int(input("How many would like to buy?: "))


total = price * quantity

tax = total/100 * 10

total = tax + total

print(f"you have brought {quantity} X {item}/s")
print(f"Your total is {total}")
print(f"Your tax is {tax}%")