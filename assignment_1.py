
num_1 = int(input("Enter number one >>> "))
num_2 = int(input("Enter numbertwo >>>"))
math = input("Please write the mathemathical opeartion '(+ , -, * /)':")
if math == "+":
    print("num_1 + num_2 =", num_1 + num_2)
elif math == "-":
    print("num_1 - num_2 =", num_1 - num_2)
elif math == "*":
    print("num_1 - num_2 =", num_1 * num_2)
elif math == "/":
    if num_2 != 0:
        print("num_1 - num_2 =", num_1 / num_2)
    else:
        print("Error: Division by zero is not allowed")

else:
    print("invalid operation")