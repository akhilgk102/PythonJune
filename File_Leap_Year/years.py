f=open("c:\\Users\\akhil\\Desktop\\PythonJune\\File_Leap_Year\\years.txt","w")
for year in range(1800,2025):
    f.write(str(year)+"\n")

# f=open("C:\\Users\\akhil\\Desktop\\PythonJune\\File_Leap_Year\\years.txt","r")
# leap_years=[]
# for leap_year in f:
#     striped_year=int(leap_year.rstrip("\n"))
#     if (striped_year%100==0 and striped_year%400==0) or (striped_year%100!=0 and striped_year%4==0):
#       leap_years.append(striped_year)
#       f=open("C:\\Users\\akhil\\Desktop\\PythonJune\\File_Leap_Year\\leap_years.txt","w")
#       f.write(str(leap_years))


f=open("C:\\Users\\akhil\\Desktop\\PythonJune\\File_Leap_Year\\years.txt","r")
centuary_years=[]
non_centuary_years=[]
for years in f:
    striped_year=int(years.rstrip("\n"))
    if striped_year%100==0:
        centuary_years.append(striped_year)
        f=open("C:\\Users\\akhil\\Desktop\\PythonJune\\File_Leap_Year\\centurary_years.txt","w")
        f.write(str(centuary_years))
    else:
     non_centuary_years.append(striped_year)
     f=open("C:\\Users\\akhil\\Desktop\\PythonJune\\File_Leap_Year\\non_centuary.txt","w")
     f.write(str(non_centuary_years))