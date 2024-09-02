name="The quick brown fox jumps over the lazy dog"
text=name.lower()
is_panagram=True
alphabets="abcdefghijklmnopqrstuvwxyz"
for ch in alphabets:
    if text.count(ch)==0:
        is_panagram=False
        break
print("It is pangram" if is_panagram==True else "It is not pangram")






# print(name.upper()) 
# print(name.capitalize())
# print(name.casefold())
# print(name.lower())
# print(name.index("a"))

# print(name.isalnum())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count("a"))
# print(name.pangram())
