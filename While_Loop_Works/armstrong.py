num=int(input("Enter the number: ")) #153
temp=num
total=0
num_count=(len(str(num)))
while(num!=0):
    digit=num%10 #3
    exponent=digit**num_count #3**3=27
    total=total+exponent
    num=num//10
if total==temp:
 print(f" {total} is a Armstrong number")
else:
   print(f"{temp} is not a Armstrong number")