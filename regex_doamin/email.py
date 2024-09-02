from re import fullmatch
f_open=open("C:\\Users\\akhil\\Desktop\\PythonJune\\regex_doamin\\email.txt","r",encoding="UTF-8")
f_write=open("C:\\Users\\akhil\\Desktop\\PythonJune\\regex_doamin\\valid_email.txt","a",encoding="UTF-8")

for lines in f_open:
    email=lines.rstrip("\n")
    pattern="[a-z0-9.]*@gmail\.com"
    matcher=fullmatch(pattern,email)
    if matcher!=None:
        f_write.write(email+"\n")