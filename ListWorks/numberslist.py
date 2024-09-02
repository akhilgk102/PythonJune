numbers=[10,12,9,8,6,7,5,25]
print(len(numbers))

# for i in range(0,len(numbers)):
#     if numbers[i]%2==0:
#         print(numbers[i])

# total=0
# for i in range(0,len(numbers)):
#     total=total+numbers[i]
# print(total)

total_odd=0
for i in range(0,len(numbers)):
    if numbers[i]%2!=0:
        total_odd=total_odd+numbers[i]
print(total_odd)