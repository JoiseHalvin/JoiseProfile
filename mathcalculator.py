import math

print("Calculator")

# user input
n1 = int(input("Give the first number: "))
n2 = int(input("Give the second number: "))

while True:
    print("(1) +\n(2) -\n(3) *\n(4) /\n(5) sin(number1/number2)\n(6) cos(number1/number2)\n(7) Change numbers\n(8) Quit")
    print("Current numbers:", n1, n2)
    choice = int(input("Please select something (1-6): "))  
    if choice == 8:
        print("Thank You!")
        break
    elif choice == 1:
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
        n3 = math.sin(n1 / n2)
        print("The result is:", n3)
    elif choice == 6:
        n3 = math.cos(n1 / n2)
        print("The result is:", n3)
    elif choice == 7:
        n1 = int(input("Give the first number: "))
        n2 = int(input("Give the second number: "))
    else:
        print("Invalid choice. Please try again.")
    
    print()