# students=dict() #Empty set of Dictionary
# print(type(students))

#dict={key:value} 
# <class Dict> :collection of elements as a key:value pair
#Dictionary key must be unique

student={"name":"Akhil","age":21,"place":"Haripad","course":"Full stack"}
# print(student["name"]) 
# print(student.keys())
# student["name"]="Arjun" # To update the values
# student["Institute"]="Luminar" # To add a new key:value in dict

# new=student.items()
# print(new)

new2=student.values()
print(new2)

for i in student:
    print(f"{i}={student[i]}")