num1=int(input("Enter the number 1: "))
num2=int(input("Enter the number 2: "))
num3=int(input("Enter the number 3: "))

if (num1>num2 and num1>num3) :
    if (num2>num3 and num2>num1):
        print(num1,num2,num3)
    else:
        print(num1,num3,num2)


elif(num2>num3 and num2>num1):
    if(num1>num2 and num1>num3):
        print(num2,num1,num3)
    else:
        print(num2,num3,num1)

elif(num3>num1 and num3>num2):
    if(num2>num1 and num2>num3):
     print(num3,num2,num1)
    else:
        print(num3,num1,num2)