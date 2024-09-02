# Write a program to print sum of all odd numbers from 1 to 100
i=0
number=0
for number in range(0,100):
    if number%2!=0:
        i=i+number #0
        number=number+2 
print(i)