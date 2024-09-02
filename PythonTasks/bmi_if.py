#Write a program to find the bmi of a person

height=int(input("Enter your height: "))
weight=int(input("Enter your weight: "))
height_metre=height/100
bmi=weight/height_metre**2
print("\n")
if bmi <19:
    print(f"BMI = {bmi} | Underweight")
elif (bmi>19 and bmi<=25 ):
    print(f"BMI = {bmi} | Normal")
elif (bmi>25 and bmi<=30):
    print(f"BMI = {bmi} | Over Weight")
elif (bmi>30):
    print(f"BMI = {bmi} | Obesity")
else:
    print("Invalid")

