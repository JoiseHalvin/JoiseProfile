print("Calculator")
# Ask the user for a number
n1 = int(input("Give the first number: "))
n2 = int(input("Give the second number: "))

while True:
    print("(1) +\n(2) -\n(3) *\n(4) /\n(5) Change numbers\n(6) Quit")
    print("Current numbers:", n1, n2)
    choice = int(input("Please select something (1-6): "))
    if choice == 6:
        print("Thank You!")
        break
    if choice == 1:
        n3 = n1 + n2
        print("The result is:", n3)
    elif choice == 2:
        n3 = n1 - n2
        print("The result is:", n3)
    elif choice == 3:
        n3 = n1 * n2
        print("The result is:", n3)
    elif choice == 4:
        n3 = n1 / n2
        print("The result is:", n3)
    elif choice == 5:
        n1 = int(input("Give the first number: "))
        n2 = int(input("Give the second number: "))
    else:
        print("Invalid choice. Please try again.")

    print()
