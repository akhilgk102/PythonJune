num=[3,2,5,7,1,9,10,4]
smallest_num=num[0]
for i in num:
    if i<smallest_num: #3<0
        smallest_num=i
print(f"{smallest_num} is Smallest")