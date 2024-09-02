num1=int(input("Enter the number1: "))
num2=int(input("Enter the number2: "))
num3=int(input("Enter the number3: "))
if (num1>num2 and num1<num3) or (num1>num3 and num1<num2):
    print(f"{num1} is Second Largest")
 
elif (num2>num1 and num2<num3) or (num2>num3 and num2<num1):
    print(f"{num2} is Second Largest")
 
elif (num3>num1 and num3<num2) or (num3>num2 and num3<num1):
    print(f"{num3} is Second Largest")
else:
    print("Invalid")