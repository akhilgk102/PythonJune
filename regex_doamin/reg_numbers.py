from re import fullmatch

f=open("C:\\Users\\akhil\\Desktop\\PythonJune\\regex_doamin\\reg_numbers.txt")

for lines in f:

    numbers=lines.rstrip("\n")

    pattern="KL[\s]?[0-9]{1,2}[\s]?[A-Z]{1,3}[\s]?[\d]{4}"

    matcher=fullmatch(pattern,numbers)

    if matcher!=None:

        f_write=open("c:\\Users\\akhil\\Desktop\\PythonJune\\regex_doamin\\valid_numbers.txt","a")

        f_write.write(str(numbers+"\n"))
