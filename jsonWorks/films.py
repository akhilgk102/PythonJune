from json import load

f=open("C:\\Users\\akhil\\Desktop\\PythonJune\\jsonWorks\\films.json")

films=load(f)

for m in films:

    print(m.get("title"))