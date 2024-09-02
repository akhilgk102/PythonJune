from re import finditer

text="ab@123pqr54xyz789cdef"

# pattern="[0-9]{3}"
# pattern="[a-z]{3}"
pattern="([c-h]|[t-z])"
matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),"===",m.group())