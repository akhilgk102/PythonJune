num=int(input("Enter the number: ")) #451
sum=0
while(num!=0):
    digit=num%10 #1
    exponent=digit**3
    sum=sum+exponent
    num=num//10 #45
print(sum)
