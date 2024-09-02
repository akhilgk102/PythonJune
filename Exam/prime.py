num=int(input("Enter the number: ")) #10
is_prime=True
for i in range(2,num): #2,3
    if num%i==0: #
        is_prime=False
    break
print(f"{num} is prime" if is_prime==True else f"{num} is Not prime")

    