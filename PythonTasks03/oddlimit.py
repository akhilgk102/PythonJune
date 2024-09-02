#Write a program to print odd numbers with starting_limit and ending_limit.

start=int(input("Enter the starting Limit: "))
stop=int(input("Enter the ending Limit: "))
for i in range(start,stop+1):
    if i%2!=0:
        print(i)