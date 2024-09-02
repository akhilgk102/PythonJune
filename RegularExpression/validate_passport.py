from re import fullmatch

passport_num=input("Enter Passport Number: ")

pattern="[A-Z][1-9][0-9][0\s][\d]{4}[1-9]"

matcher=fullmatch(pattern,passport_num)

print("Invalid" if matcher==None else "Valid")