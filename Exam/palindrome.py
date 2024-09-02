num=int(input("Enter the number: "))
temp=num
result=0
while(num!=0):
    digit=num%10
    result=result*10+digit
    num=num//10
if result==temp:
    print(f"{temp} is Palindrome")
else:
        print(f"{temp} is not Palindrome")

