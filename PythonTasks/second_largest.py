num1=int(input("Enter the number 1: "))
num2=int(input("Enter the number 2: "))
num3=int(input("Enter the number 3: "))
if num1>num2 and num1>num3:
    if num2>num3:
      print(f"{num2} is  Second Largest")
    else:
        print(f"{num3} is Second Largest")
    
elif num2>num1 and num2>num3:
    if num1>num3:
      print(f"{num1} is Second Largest")
    else:
       print(f"{num3} is Second Largest")

elif num3>num1 and num3>num2:
    if num2>num1:
     print(f"{num2} is Largest")
    else:
       print(f"{num1} is Second Largest")
elif num1==num2==num3:
   print("Three numbers are equal")
