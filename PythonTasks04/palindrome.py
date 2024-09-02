num1=int(input("Enter the number: ")) #123
temp=num1
total=0
while(num1!=0):
    digit=num1%10 #3 #2
    total=total*10+digit #3 
    num1=num1//10 #12
if total==temp:
    print("Palindrome")
else:
    print("not")
