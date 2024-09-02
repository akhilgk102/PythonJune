num=[4,6,12,5,1,8,10,11,7]

largest_num=num[0]

second_largest_num=num[0]

for i in num:

    if i > largest_num and i >second_largest_num:

        second_largest_num=largest_num

        largest_num=i

    elif i>second_largest_num and i<largest_num:
        
        second_largest_num=i

print(second_largest_num)