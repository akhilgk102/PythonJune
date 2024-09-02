f=open("C:\\Users\\akhil\\Desktop\\PythonJune\\FileOperations\\students.txt","r")

students_list=[]
for students in f:
    students_list.append(students.rstrip("\n"))
print(students_list)