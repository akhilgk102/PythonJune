# Step 1: To write numbers from 50 - 200
f=open("C:\\Users\\akhil\\Desktop\\PythonJune\\PythonTasks07\\numbers.txt","a")
for num in range(50,201):
    f.write(str(num)+"\n")


# Step 2: To write the even numbers to a txt file
f=open("C:\\Users\\akhil\\Desktop\\PythonJune\\PythonTasks07\\numbers.txt","r")
even_numbers=[]
for num in f:
    striped_num=int(num.rstrip("\n"))
    if striped_num%2==0:
        even_numbers.append(striped_num)
    f=open("C:\\Users\\akhil\\Desktop\\PythonJune\\PythonTasks07\\even_nmbrs.txt","w")
    f.write(str(even_numbers))

# Step 3 To write the odd numbers to txt file
f=open("C:\\Users\\akhil\\Desktop\\PythonJune\\PythonTasks07\\numbers.txt","r")
odd_numbers=[]
for numbers in f:
    striped_number=int(numbers.rstrip("\n"))
    if striped_number%2!=0:
        odd_numbers.append(striped_number)
    f=open("c:\\Users\\akhil\\Desktop\\PythonJune\\PythonTasks07\\odd_numbers.txt","w")
    f.write(str(odd_numbers))
