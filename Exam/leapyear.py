year=1800
total=0
while(year<=2028):
    if(year%100==0 and year%400==0) or (year%100!=0 and year%4==0):
     print(year)
    year=year+4