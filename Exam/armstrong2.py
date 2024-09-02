num=int(input("Enter the number: ")) #153
temp=num
result=0
num_count=len(str(num))
while(num!=0):
    digit=num%10 #3, 5
    exponent=digit**num_count #3^3=27, 5^3=125, 
    result=result+exponent #0+27+125
    num=num//10 #15
if temp==result:
    print(f"{temp} is Armstrong")
else:
    print(f"{temp} is not Armstrong")
