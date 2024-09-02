from  re import fullmatch

vehicle_number=str(input("Enter Vehicle number: "))

pattern="(KL)(-)?[0-9]{2}(-)?[A-Z]{1,2}(-)?[\d]{4}"

matcher=fullmatch(pattern,vehicle_number)

print("Invalid" if matcher==None else "Valid")