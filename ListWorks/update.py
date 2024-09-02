#numbers=[1,2,[3,(100,200,300),4],5,6] >>>>> numbers=[1,2,[3,4,(100,150,200,300)],5,6]

numbers=[1,2,[3,(100,200,300),4],5,6]

new=numbers[2]

delete=new.pop()

new.insert(1,delete)
print(new)

numbers[2]=new
print(numbers)

new1=numbers[2][2]
l=list(new1)
l.insert(1,150)
l1=tuple(l)
numbers[2][2]=l1  
print(numbers)