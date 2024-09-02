#Print the factorial of a number
import random
num=random.randint(0,10)
fact=1
for i in range(1,num+1):
    fact=fact*i
print(f"{num}!={fact}")