arr=[
    [10,20],
    [20,30],
    [40,53]
    ]

# evens=[num for lst in arr for num in lst if num%2==0]
evens=[]
for lst in arr:

    for num in lst:

        if num%2==0:

            evens.append(num)
            
print(evens)