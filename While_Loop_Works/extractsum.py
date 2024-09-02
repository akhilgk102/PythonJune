#Write a progrm to extract the digits and sum them
num=int(input("Enter the number: ")) #451
sum=0
while(num!=0):
    digit=num%10 #1
    num=num//10 #45
    sum=digit+sum
print(sum)
