#Update the couse as fullstack in students in iteration.

student={"Name":"Akhil G Krishnan","Place":"Haripad","Age":21}
print(student["Age"])
new=[]
for i in student:
    if i=="Place":
        new.append(i)

for key in new:
    student.pop(key)

for i in student:
    print(f"{i} = {student[i]}")