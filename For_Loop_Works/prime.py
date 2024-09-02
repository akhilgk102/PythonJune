num=int(input("Enter the number: "))
is_Prime=True
for i in range(2,num):
    if num%i==0:
     is_Prime=False
     break
print(f"{num} is Prime number"if is_Prime==True else f"{num} is Not Prime")