# #Print First 10 natural numbers using while loop
# i=0
# while(i<=10):
#     print(i)
#     i=i+1

n=5
for i in range(1,n+1,1):
    for j in range(1,i+1):
        print(j,end="")
    print("")
