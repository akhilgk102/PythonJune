from json import load
f=open("C:\\Users\\akhil\\Desktop\\PythonJune\\jsonWorks\\countrys.json",encoding="UTF-8")
info=load(f)

    # Q1 Total countries count?
# print(len(info)) 

    # Q2 Total countries names?
total_countries=[i.get("name")for i in info]
# print(total_countries)

    # Q3  Print only asian countries
only_asian_countries=[i.get("name")for i in info if i.get("region")=="Asia"]
# print(only_asian_countries)

    # Q4 Continents with countries count
continent_summary={}
for i in info:
    if i.get("region") in continent_summary:
        continent_summary[i.get("region")]+=1
    else:
        continent_summary[i.get("region")]=1
# print(continent_summary)

    #Q5 Countries with their capitals
countries_capital={}
for i in info:
    if i.get("name") in countries_capital:
        countries_capital[i.get("name")]=i.get("capital")
    else:
        countries_capital[i.get("name")]=i.get("capital")
# print(countries_capital)

    #Q6 Most populated country
def most_populated(country):
    return country.get("population")

most_populated_country=max(info,key=most_populated)
# print(most_populated_country.get("name"),most_populated_country.get("population"))

    #Q7 Least populated country
least_populated_country=min(info,key=most_populated)
# print(least_populated_country.get("name"),least_populated_country.get("population"))

    #Q8 Countries with population
population_summary={}
for i in info:
    if i.get("name") in population_summary:
        population_summary[i.get("name")]=i.get("population")
    else:
        population_summary[i.get("name")]=i.get("population")
# print(population_summary)


    #Q9 Countries with curriency names
currency_summary = {}
for i in info:
    country_name=i.get("name")
    if i.get("currencies") and country_name:
        currency_name=i["currencies"][0].get("name")
        if currency_name:
            currency_summary[country_name]=currency_name
# print(currency_summary)


    #Q10 Countries with alpha3code
code_summary={}
for i in info:
    if i.get("name") in code_summary:
        code_summary[i.get("name")]=i.get("alpha3Code")
    else:
        code_summary[i.get("name")]=i.get("alpha3Code")
# print(code_summary)

    #Q11 Largest country by area
def country_area(area):
    return area.get("area",0)

largest_country=max(info,key=country_area)
# print(largest_country.get("name"),largest_country.get("area"))

smallest_country=min(info,key=country_area)
# print(smallest_country.get("name"),smallest_country.get("area"))

    #Q12 Countries with calling code
numeric_code_summary={}
for i in info:
    if i.get("name") in numeric_code_summary:
        numeric_code_summary[i.get("name")]=i.get("callingCodes")
    else:
        numeric_code_summary[i.get("name")]=i.get("callingCodes")
# print(numeric_code_summary)

    # Q13 Specific country information
# country=str(input("Enter your country name: "))
# for i in info:
#     if country.capitalize() == i.get("name"):
#         print(i)

    #Q14 Specific country with their capital
# country=str(input("Enter your country name: "))
# for i in info:
#     if country.capitalize() == i.get("name"):
#         print(country,"Capital : ",i.get("capital"))

    #Q15 Countries with "island" in their country names
island_countries=[i.get("name")for i in info if "Island" in i.get("name")]
# print(island_countries)

    #Q16  Countries that are independent
independent_countries=[i.get("name")for i in info if i.get("independent")==True]
# print(independent_countries)

    #Q17  Countries that are not independent
not_independent_countries=[i.get("name")for i in info if i.get("independent")==False]
# print(not_independent_countries)

    #Q18 World population
world_population=sum([i.get("population")for i in info])
# print(f"World Population = {world_population}")

    #Q19 largest continent
region_summary={}
for i in info:
    region_name=i.get("region")
    if region_name in region_summary:
        region_summary[region_name]+=i.get("area",0)
    else:
        region_summary[region_name]=i.get("area",0)
# print(region_summary)
value_key=[(v,k)for k,v in region_summary.items()]
print(max(value_key))
    
    # Q20 Countries spoke english
english_countries=[i.get("name")for i in info  for l in i.get("languages") if l.get("name")=="English"]
# print(english_countries)
