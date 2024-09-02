num1=int(input("Enter the number 1: "))
num2=int(input("Enter the number 2: "))
num3=int(input("Enter the number 3: "))
if (num1>num2>num3) or (num3>num2>num1):
    print(num2)
elif (num2>num1>num3) or (num3>num1>num2):
    print(num1)
elif (num2>num3>num1) or (num1>num3>num2):
    print(num3)