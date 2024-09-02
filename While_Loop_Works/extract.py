#Write a progrm to extract the digits
num=int(input("Enter the number: ")) #451
while(num!=0):
    digit=num%10 #1
    print(digit)
    num=num//10 #45
