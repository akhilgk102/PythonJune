def is_palindrome(num1): #121
    temp=num1
    total=0
    sum=0
    while(num1!=0):
        digit=num1%10  #1 #2
        sum=sum*10+digit #0+1+12
        num1=num1//10 #12
    if sum==temp:
        return True
    else:
        return False
print(is_palindrome(121))