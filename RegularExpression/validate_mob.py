 #Write code for validate mobile number with country code

from re import fullmatch

mob_number=input("Enter mobile number: ")

pattern="(91)\s?[6-9]\d{9}"

matcher=fullmatch(pattern,mob_number)

print("Invalid" if matcher==None else "Valid")