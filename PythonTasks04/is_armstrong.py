def is_armstrong (num1): #153
    temp=num1
    count=(len(str(num1)))
    total=0
    while(num1!=0):
        digit=num1%10 #3 #5 #1
        sum=digit**count #3^3=27 5^3=125 1^3=14
        total=total+sum #153
        num1=num1//10 
    if temp==total:
        return True
    else:
        return False
print(is_armstrong(9474))