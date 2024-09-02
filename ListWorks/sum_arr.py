arr=[
    [10,20],
    [20,30],
    [40,53]
    ]
# sums=[]

# for lst in arr:

#     for num in lst:

#         sums.append(num)

#         b=sum(sums)

# print(b)

sum_of_nums=[num for lst in arr for num in lst ]

print(sum_of_nums)
