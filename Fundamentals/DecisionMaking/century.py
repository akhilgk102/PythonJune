year=int(input("Enter the Year: "))
if year%100==0:
    print(f"{year} is Century Year")
else:
    print(f"{year} is Non Century Year")