print("My simple calci ;) ")
print("1. Lemme Add")
print("2. Lemme Subtract")
print("3. Lemme Multiply")
print("4. Lemme Divide")

choice = int(input("Enter choice (1-4): "))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    print("Result:", num1 + num2)
elif choice == 2:
    print("Result:", num1 - num2)
elif choice == 3:
    print("Result:", num1 * num2)
elif choice == 4:
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("What ya how can you divide anything by zero? :P")
else:
    print("Keep it within ur reach! :/ ")