#   Wap the count of even and odd numbers in the list

num=[1,2,3,4,5,6,7,8,9,10]
odd_count=0
even_count=0
for i in num:
    if i%2==0:
        odd_count=odd_count+1
    else:
        even_count=even_count+1
print(f"Odd count={odd_count}\nEven Count={even_count}")