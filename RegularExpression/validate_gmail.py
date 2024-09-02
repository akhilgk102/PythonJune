# Write a program to find the gmail is valid or not

from re import fullmatch

gmail=input("Enter E-mail: ")

# pattern="[a-zA-Z][a-zA-Z0-9._]*(@gmail.com|@GMAIL.COM)"
pattern="[\w][\w._]*(@gmail.com|@GMAIL.COM)"

matcher=fullmatch(pattern,gmail)

print("Invalid" if matcher==None else "Valid")