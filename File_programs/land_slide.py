total_deaths=0
f=open("C:\\Users\\akhil\\Desktop\\PythonJune\\File_programs\\land_slides.txt","r")
data=[]
for lines in f:
    striped=lines.rstrip("\n").split(" ")
    lan_slide={"state":striped[0],"year":striped[1],"deaths":int(striped[2])}
    data.append(lan_slide)


# which state mor death
state_summary={}
for dic in data:
    state=dic.get("state")
    death_count=dic.get("deaths")

    if state in state_summary:
        state_summary[state]+=death_count
    else:
        state_summary[state]=death_count
max_death=max(state_summary,key=state_summary.get)
print(f"Most deaths state : {max_death}")


# wich year more death
year_summary={}
for dic in data:
    year=dic.get("year")
    death=dic.get("deaths")
    if year in year_summary:
        year_summary[year]+=death
    else:
        year_summary[year]=death
max_year = max(year_summary, key=year_summary.get)
print(f"Most deaths year : {max_year}")


# Total death count
for dic in data:
    death_count=dic.get("deaths")
    total_deaths+=death_count
print("Total Deaths = ",total_deaths)
