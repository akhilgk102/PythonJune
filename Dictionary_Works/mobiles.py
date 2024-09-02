#Create a dictionary mobile with keys name, brand,price and is_available

mobiles={"Name":"Samsung S25","Brand":"Samsung","Price":120000,"is_available":True}

for k,v in mobiles.items():

    print(k,v)

print(mobiles.get("Name")) #get method returns invalid key as "None"
print(mobiles.values()) #Returns the values