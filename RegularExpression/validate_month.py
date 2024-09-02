from re import fullmatch

month=input("Enter Month: ")

pattern="(0?[1-9]|1[0-2])"

matcher=fullmatch(pattern,month)

print("Invalid" if matcher==None else "Valid")