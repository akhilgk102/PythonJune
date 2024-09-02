#Write a program to find the EMI of a loan 
# EMI = P x R x (1+R)^N / ((1+R)^N-1)
amount=100000
tenture=12
interst=7.2
monthly_interst=interst/12/100
emi =(amount*monthly_interst*(1+monthly_interst)**tenture) / ((1+monthly_interst)**tenture-1) 
print(f"Loan Amount= Rs {amount}\nLoan Tenture={tenture} Months\nInterst Rate={monthly_interst}\nEMI = ₹ {emi}")