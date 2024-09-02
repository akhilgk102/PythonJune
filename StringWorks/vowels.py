name="pneumonoultramicroscopicsilicovolcanoconiosis"
small=name.lower()
v_count=0
vowels="aeiou"
for ch in name:
    if vowels.count(ch)!=0:
        v_count=v_count+1
print(v_count)