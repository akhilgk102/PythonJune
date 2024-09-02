from re import fullmatch

variable_name=str(input("Enter the Variable name: "))

pattern="[a-zA-Z][\w_]*"

matcher=fullmatch(pattern,variable_name)

print("Invalid" if matcher==None else "Valid")