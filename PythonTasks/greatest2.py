num1=int(input("Enter the number 1: "))
num2=int(input("Enter the number 2: "))
num3=int(input("Enter the number 3: "))
if num1>num2 and num1>num3:
    print(f"{num1} is Largest")
    
elif num2>num1 and num2>num3:
    print(f"{num2} is Largest")

elif num3>num1 and num3>num2:
    print(f"{num3} is Largest")
