#Write a program to find the bmi of a person

height=int(input("Enter your height: "))
weight=int(input("Enter your weight: "))
height_metre=height/100
bmi=weight/height_metre**2
print("\n")
print(f"Height = {height}\nWeight = {weight}\nBMI = {bmi}")