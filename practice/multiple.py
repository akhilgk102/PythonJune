num1=100
num2=200
num3=300
print(num1>num2 and num1>num3) #False
print(num2>num1 and num2>num3) #False
print(num3>num1 and num3>num2) #True
print(num1==num2 and num1==num3) #False
print(num1!=num2 and num1!=num3) #True

print("\n")
print(num1>num2 or num1>num3) #False
print(num2>num1 or num2>num3) #True
print(num3>num1 or num3>num2) #True
print(num1!=num2 or num2!=num3) #True
print(num1==num2 or num1==num3) #False

print("\n")
print(not num1>num2) #True
print(not num3>num1) #False
print(not num3<num1) #True
print(not num1==num2) #True
print(not num1!=num2) #False
