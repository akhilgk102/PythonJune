arr=[
    [10,11,12],
    [12,13,14],
    [15,16]

]

greater=[num for lst in arr for num in lst if num>11]
print(greater)