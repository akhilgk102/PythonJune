name = "RACECAR"
count = len(name)

for i in range(count):
    left = i
    right = i
    while left >= 0 and right < count and name[left] == name[right]:
        current_palindrome = name[left:right + 1]
        print(current_palindrome)
        left -= 1
        right += 1
