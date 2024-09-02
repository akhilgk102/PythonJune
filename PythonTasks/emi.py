#Write a program to calculate
# Monthly EMI
# Total Payment
# Total Interst Payable

principal_amount=int(input("Enter the Principal Amount: "))
loan_tenure=int(input("Enter the Loan Tenure: "))
loan_interest=int(input("Enter the Loan Interest For Year: "))

monthly_interst=loan_interest/12/100
emi=(principal_amount*monthly_interst*(1+monthly_interst)**loan_tenure) / ((1+monthly_interst)**loan_tenure-1)
total_payment=emi*loan_tenure
total_interest=total_payment-principal_amount
print(f"Monthly EMI = Rs {emi}\nTotal Payment = Rs {total_payment}\nTotal Interest Payable = Rs {total_interest}")