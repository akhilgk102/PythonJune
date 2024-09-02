numbers=[10,10,20,20,20,21,22,23]

number=set(numbers)

for num in number:

    print(num,"=",numbers.count(num)) #Numbers Count

for num in numbers:

    if numbers.count(num)==1:

        print(num,end=",") #Unique numbers