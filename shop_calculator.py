m1 = 0
m2 = 0
p = 0
t = 0
c = 0
n1 = 0

while True:

    k = int(input("""
    ===== SHOP MENU =====

    1. Enter product price
    2. Enter product quantity
    3. Calculate total price
    4. Enter discount
    5. Calculate final price
    6. Display final price
    7. Enter customer payment
    8. Calculate customer change
    9. Exit

    Please choose an option: 
    """))

    if k == 1:
        m1 = int(input("Enter product price: "))

    elif k == 2:
        m2 = int(input("Enter product quantity: "))

    elif k == 3:
        if m1 > 0 and m2 > 0:
            p = m1 * m2
            print("Total price:", p)
        else:
            print("Please enter price and quantity first!")

    elif k == 4:
        if p > 0:
            t = int(input("Enter discount amount: "))
        else:
            print("Calculate total price first!")

    elif k == 5:
        if p > 0:
            if t <= p:
                c = p - t
                print("Final price:", c)
            else:
                print("Discount cannot be greater than total price!")
        else:
            print("Calculate total price first!")

    elif k == 6:
        print("Final price:", c)

    elif k == 7:
        if c > 0:
            n1 = int(input("Enter customer payment: "))
        else:
            print("Calculate final price first!")

    elif k == 8:
        if n1 >= c and c > 0:
            b = n1 - c
            print("Customer change:", b)
        elif n1 < c and n1 > 0:
            print("Not enough money!")
            print("Remaining amount:", c - n1)
        else:
            print("Enter customer payment first!")

    elif k == 9:
        print("Goodbye!")
        break

    else:
        print("Invalid option!")
