arr=[0,2,3,4]

n=len(arr)

sum_of_n=n*(n+1)/2

current_sum=sum(arr)

missing_number=sum_of_n-current_sum

print(int(missing_number))


# arr=[0,1,3,4]

# new=[]

# previous=arr[0]

# current=arr[1]

# for num in arr:

#     if current-previous!=1:

#         new.append(previous+1)
    
# print(new)
