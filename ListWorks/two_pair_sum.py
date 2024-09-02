numbers=[2,3,4,5]
sum=0
result=7
for i in range(0,len(numbers)):
    sum=sum+numbers[i]
    if sum==result:
        print(sum)