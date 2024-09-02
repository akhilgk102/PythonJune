#Print the employee total slary if he/she works extra days

employee={"Nmae":"Hari","Dept":"R&D","Salary":50000,"Combo_offer":1000,"extra_working_days":2}

if "extra_working_days" in employee:

    extra_salary=employee.get("Combo_offer")*employee.get("extra_working_days")+employee.get("Salary")

    print(extra_salary)

else:

    print(employee.get("Salary"))