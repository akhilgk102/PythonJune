num=[13,5,7,9,40,12,90]


smallest_num=num[0]

second_small=num[-1]

for i in num:

    if i < second_small and i <smallest_num: #3<1 and 3<3

        second_small=smallest_num

        smallest_num=i

    elif i<second_small and i >smallest_num: #3<1 and 3>1

        smallest_num=i

print(second_small)