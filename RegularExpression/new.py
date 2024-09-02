#1. Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).

from re import finditer

text="helloAKHIL2255@3*b"

pattern="[ab]"

matcher=finditer(pattern,text)

for m in matcher:

    print(m.start(),"==",m.group())
