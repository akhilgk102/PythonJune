number = [0, 2, 6, 8]

new = []
previous = number[0]


for i in range(1, len(number)):

    current = number[i]

    if current - previous != 2:

        new.append(previous + 2)
        
    previous = current

print(new)
