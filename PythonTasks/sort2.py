num1=int(input("Enter the number 1: "))
num2=int(input("Enter the number 2: "))
num3=int(input("Enter the number 3: "))
if num1>num2 and num1>num3:
      result=num1
elif num2>num1 and num2>num3:
    result=num2
elif num3>num1 and num3>num1:
    result=num3
    result.sort()
    print(result)

 