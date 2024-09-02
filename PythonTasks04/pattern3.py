for row in range(7):
    for col in range(row,6):
        print("",end=" ")
    for col in range(row):
        print("*",end=" ")
    print()