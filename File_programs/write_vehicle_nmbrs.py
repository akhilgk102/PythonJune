vehicle_numbers=["KL29M1998","KL29T3654","KL29E5228"]

f=open("C:\\Users\\akhil\\Desktop\\PythonJune\\File_programs\\vehicle_nmrs.txt","w")

for number in vehicle_numbers:

    f.write(number+"\n")