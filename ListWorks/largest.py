num=[1,2,3,4,5,6,7,8,9,10]
largest_num=num[0]
for i in num:
    if i > largest_num:
        largest_num=i
print(f"{largest_num} is the Largest")