olympic_medal_count = [
    {"country": "United States", "gold": 39, "silver": 41, "bronze": 33},
    {"country": "China", "gold": 38, "silver": 32, "bronze": 18},
    {"country": "Japan", "gold": 27, "silver": 14, "bronze": 17},
    {"country": "Great Britain", "gold": 22, "silver": 21, "bronze": 22},
    {"country": "Russia", "gold": 20, "silver": 28, "bronze": 23},
    {"country": "Australia", "gold": 17, "silver": 7, "bronze": 22},
    {"country": "Netherlands", "gold": 10, "silver": 12, "bronze": 14},
    {"country": "France", "gold": 10, "silver": 12, "bronze": 11},
    {"country": "Germany", "gold": 10, "silver": 11, "bronze": 16},
    {"country": "Italy", "gold": 10, "silver": 10, "bronze": 20}
]

# Q1 Country mist most number of gold medals
# def most_gold(country):
#     return country.get("gold")
# most_golds=max(olympic_medal_count,key=most_gold)
# total_gold=most_gold(most_golds)
# print(most_golds["country"],"=",total_gold,"Golds")
    


# Q2 Medal count of each countries 
# for country in olympic_medal_count:
#     all_medals=country.get("gold")+country.get("silver")+country.get("bronze")
#     print(country.get("country"),"=",all_medals,"Medals")



# Q3 Country with least number of medals
# def total_medal(country):
#     return country.get("gold")+country.get("silver")+country.get("bronze")
# least=min(olympic_medal_count,key=total_medal)
# least_total_medals=total_medal(least)
# print(f"{least['country']} : {least_total_medals} Medals")


# Q4 Sort countries with medal count
# def country(gold):
#     return gold.get("gold")+gold.get("silver")+gold.get("bronze")
# sorted_county=sorted(olympic_medal_count,key=country,reverse=True)
# for sorting in sorted_county:
#     all_medals=country(sorting)
#     print(f"{sorting['country']} = {all_medals}")

