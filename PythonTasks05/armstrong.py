numbers=[151,153,154,370,371,372,373,16341,1635]
sum=0
for number in numbers:
    digit=number%10 #1 #5 #1
    exponent=digit**3 #0+1 5 1
    sum=sum+exponent
    number=number//10 #15
if sum==number:
    print(f"{sum} is Armstrong number")

else:
    print(f"{sum} is  not Armstrong number")