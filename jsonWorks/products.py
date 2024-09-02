from json import load

f=open("C:\\Users\\akhil\\Desktop\\PythonJune\\jsonWorks\\products.json",encoding="UTF-8")

items=load(f)

# print(len(items)) # The total products

product=[i.get("title")for i in items]
# print(product)

jewelery_titles=[i.get("title")for i in items if i.get("category")=="jewelery"]
# print(jewelery_titles)

jewelery_products=[i.get("title")for i in items if i.get("category")=="jewelery"]
# print(jewelery_products)

above100=[i.get("title")for i in items if i.get("price")>100]
# print(above100)

between100and150=[i.get("title")for i in items if i.get("price")>=100 and i.get("price")<=150]
# print(between100and150)

def most_rating(dic):
    return dic.get("rating").get("count")

max_review=max(items,key=most_rating)
# print(max_review.get("title"),max_review.get("rating").get("count"))

min_review=min(items,key=most_rating)
print(min_review.get("title"),min_review.get("rating").get("count"),"Ratings")