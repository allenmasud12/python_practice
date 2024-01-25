num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
operator= input("Enter Operator: ")

if operator == "+":
    print("The Addition is: ",num1+num2)
elif operator == "-":
    print("The Subtraction is: ", num1-num2)
elif operator == "*":
    print("The Multiplication is: ", num1*num2)
elif operator == "/":
    print("The Division is: ", abs(num1/num2))
else:
    print("Invalid operator!")