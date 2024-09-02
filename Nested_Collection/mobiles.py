mobiles=[

    {"id":100,"title":"s23 ultra","brand":"samsung","price":125000,"network":"5g"},
    {"id":101,"title":"s23","brand":"samsung","price":54000,"network":"4g"},
    {"id":102,"title":"edge14pro","brand":"moto","price":25000,"network":"5g"},
    {"id":103,"title":"edgeneo","brand":"moto","price":22000,"network":"4g"},
    {"id":104,"title":"redminote13pro","brand":"mi","price":25000,"network":"5g"},
    {"id":105,"title":"redmi13","brand":"mi","price":12000,"network":"4g"},
]

# # all_mobiles={mobile.get("brand") for mobile in mobiles}

# # all_mobile_names=[mobile_name.get("title")for mobile_name in mobiles]

# # print(all_mobiles)

# # print(all_mobile_names)

# samsung_mobiles=[mob.get("title")for mob in mobiles if mob.get("brand")=="samsung"]

# # print(samsung_mobiles)

# #print all mobiles priice range of 23k to 40k

# # mobile_price=[mob.get("title")for mob in mobiles if mob.get("price")>=23000 and mob.get("price")<=40000]


# mobile_price=[mob.get("title")for mob in mobiles if mob.get("price") in range(23000,40000)]


# # print(mobile_price)

# max_price=0

# for mob in mobiles:

#     if mob.get("price")>max_price:

#         max_price=mob.get("price")

# max_price_mobile=[mob.get("title")for mob in mobiles if mob.get("price")==max_price]

# costly_mobile=max(mobiles,key=lambda mob: mob.get("price"))

# print(costly_mobile)


# # print(max_price_mobile)


def get_price(mob):

    return mob.get("price")

highest=max(mobiles,key=get_price)

print(highest)

