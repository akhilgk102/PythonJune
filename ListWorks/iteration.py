#return iteration condition
#map if num>5 => num+1 if num<5 >= num-1

arr=[2,3,5,6,7,4,1]

# mapped_list=[]

# for num in arr:

#     if num>5:

#         mapped_list.append(num+1)

#     else:
#         mapped_list.append(num-1)

mapped_list=[num+1 if num>5 else num-1 for num in arr]

print(mapped_list)