num=int(input("Enter the number: "))
previous=0
current=1
next=previous+current
is_Fibo=False
while(next<=num):
    next=previous+current
    previous=current
    current=next
    if next==num:
     is_Fibo=True
     break
print(f"{num} is Fibonacci" if is_Fibo==True else f"{num} is not Fibonacci")