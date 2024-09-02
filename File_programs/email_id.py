email_id=[
            "akhil@gmail.com",
            "arjun@gmail.com",
            "riya@gmail.com",
            "vishnu@gmail.com",
            "yadhu@gmail.com",
]

f=open("C:\\Users\\akhil\\Desktop\\PythonJune\\File_programs\\email_id.txt","w")

for email in email_id:

    f.write(email+"\n")