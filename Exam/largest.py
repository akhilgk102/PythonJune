#Read two numbers from num1,num2
# Print largest
# If both are equal print both are equal

num1=int(input("Enter the number 1: "))
num2=int(input("Enter the number 2: "))
if num1>num2:
    print(f"{num1} is Largest")

elif num2>num1:
    print(f"{num2} is Largest")

elif num2==num1:
    print("Both are equal")