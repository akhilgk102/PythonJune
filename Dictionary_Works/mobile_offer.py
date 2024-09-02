#Create a dictionary with mobiles and check the offer price.

mobiles={"Name":"Samsung S25","Brand":"Samsung","Price":120000,"is_available":True}

mobiles["Offer"]=5250

if "Offer" in mobiles:

    selling_price=mobiles.get("Price")-mobiles.get("Offer")

    print("Rs",selling_price)

else:

    selling_price=mobiles.get("Price")

    print("Rs",selling_price)