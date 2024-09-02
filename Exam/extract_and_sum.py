#Write a progrm to extract the digits and sum them and exclude if any even numbers
num=int(input("Enter the number: ")) #15
sum=0
while(num!=0):
     digit=num%10 #5, 1
     if digit%2!=0:
      sum=sum+digit #0+5, 5+1
     num=num//10 #1 0
print(sum)
