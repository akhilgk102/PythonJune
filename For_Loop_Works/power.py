#power ranger
#Print the pattern of a number 
num=int(input("Enter the number: "))
pattern=0
total=0
for i in range(1,num+1):
    pattern=pattern*10+num
    total=total+pattern
    print(pattern)
print(f"Total = {total}")