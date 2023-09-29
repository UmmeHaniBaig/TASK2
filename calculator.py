print("select an operation to perform")
print("1-Addition")
print("2-subtraction")
print("3-multiplication")
print("4-division")
number=input("Enter a number")
if number=="1":
    num1=input("Enter first number: ")
    num2=input("Enter second number: ")
    print("The result of these two are "+ str(int(num1) + int(num2)))
elif number=="2":
    num1=input("Enter first number: ")
    num2=input("Enter second number: ")
    print("The result of these two are "+ str(int(num1) - int(num2)))

elif number=="3":
    num1=input("Enter first number: ")
    num2=input("Enter second number: ")
    print("The result of these two are "+ str(int(num1) * int(num2)))

elif number=="4":
    num1=input("Enter first number: ")
    num2=input("Enter second number: ")
    print("The result of these two are "+ str(int(num1) / int(num2)))

else:
    print("You enter invalid")

    
