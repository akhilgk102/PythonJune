from re import fullmatch

date=input("Enter date: ")

pattern="(0?[1-9]|1[\d]|2[\d]|3[0-1])"

matcher=fullmatch(pattern,date)

print("Invalid" if matcher==None else "Valid")