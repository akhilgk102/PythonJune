height=int(input("Enter the height: "))
weight=int(input("Enter the weight: "))
height_metre=height/100
bmi=weight/height_metre**2
if bmi<19:
    print(f"BMI = {bmi} | Under weight")
elif bmi>19 and bmi<=25:
    print(f"BMI = {bmi} |  Normal")
elif bmi>25 and bmi<=30:
        print(f"BMI = {bmi} |  Over weight")
else:
        print(f"BMI = {bmi} |  Obesity")