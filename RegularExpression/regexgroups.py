from re import finditer

text="abc@!-=?#123 Kfg98hpM"

# pattern="[aKf]"  #Check either a, K or f

# pattern="[a-k]" #Check for alphabets from a to k

# pattern="[a-z]" #Check for all lowercase alphabets

# pattern="[A-Z]" #Check for all uppercase alphabets 

# pattern="[A-Za-z]" #Write a pattern for matching all alphabets

# pattern="[0-9]" #Check for digits

# pattern="[a-zA-Z0-9]" #Check for multiple

# pattern="[^0-9]" #^ It excludes

# pattern="[\s]" #Check for space

pattern="[^a-zA-Z0-9\s]" #Print special characters

matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),"==",m.group())