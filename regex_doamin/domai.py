from re import fullmatch

f=open("c:\\Users\\akhil\\Desktop\\PythonJune\\regex_doamin\\domain.txt",encoding="UTF-8")

pattern="[\w\W]*\.com"

for i in f:

    domain=i.rstrip("\n")

    matcher=fullmatch(pattern,domain)
    
    if matcher!=None:
        print(domain)
