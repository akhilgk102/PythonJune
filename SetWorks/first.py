#empty set= s=set()
# Duplicates not allowed 
# Elements are unordered 
# Cannot fetch a object using index position in set object
# Mutable: We can add or remove the elements in the set.


name={"Akhil","Vishnu","Shameer","Akhil"}
print(type(name))

add=name.add("ravi")
delete=name.remove("Shameer")

print(name)

b=set()
print(type(b))