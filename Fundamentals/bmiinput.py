height=int(input("Enter your height: "))
weight=int(input("Enter your weight: "))
height_metre=height/100
bmi=weight/height_metre**2
print("\n")
print(f"Height = {height}\nWeight = {weight}\nBMI = {bmi}")
if bmi >25:
    print("Overweight")
elif bmi<10:
    print("Underweight")
else:
    print("Normal")