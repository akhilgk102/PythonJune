arr=[
    [10,20],
    [20,30],
    [40,53]
    ]

# numbers=[]

# for lst in arr:

#     for num in lst:

#         if num>15:

#             numbers.append(num)
            
# print(numbers)

numbers=[num for lst in arr for num in lst if num>15]

print(numbers)