c0 = int(input("enter a number"))

steps = 0
if c0 <= 0:
    print("The number must be a non-negative and non-zero integer.")

else:
    while c0 != 1:
        print(c0)
        if c0 % 2 == 0:
            c0 = c0 // 2
        else:
            c0 = 3 * c0 + 1
        steps += 1

    # print(c0)

    print("Steps=", steps)