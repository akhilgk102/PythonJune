stud_name=input("Enter student name: ")
mark1=int(input("Enter Mark1: "))
mark2=int(input("Enter Mark2: "))
mark3=int(input("Enter Mark3: "))
total=mark1+mark2+mark3
count=len(str(total))
#Method 3 total=int(mark1)+int(mark2)+int(mark3)
avg=total/count
print(f"Student name: {stud_name}\n Total Mark is{total}\n Average Mark is{avg}")