#Write a program to validate PAN Card
# <<<<Rules>>>
# 1. first 3 charcters are alphabets
# 2. 4th place PCAFHT
# 3. 5th place A-Z
# 4. 4 digits
# A-Z

from re import fullmatch

pan_number=(input("Enter PAN Number: "))

pattern="[A-Z]{3}[PCAFHT][A-Z][\d]{4}[A-Z]"

matcher=fullmatch(pattern,pan_number)

print("Invalid" if matcher==None else "Valid")