expenses=[12000,13000,14000,21000,25000,30000]
expenses_count=len(expenses)
print(expenses_count) #count
sum=0

for i in range(0,expenses_count):
    sum=sum+expenses[i]
print(sum) #total or sum

average=sum/expenses_count
print(average) #average