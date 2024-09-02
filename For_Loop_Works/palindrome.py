#Write a program to check the number is palindrome or not

num=int(input("Enter the number: "))
temp=num
result=0
while(num!=0):
    digit=num%10
    result=result*10+digit
    num=num//10
print(result)

if result==temp:
    print(f"{result} is palindrome")
else:
    print(f"{result} is Not palindrome")