vowels="aeiou"
words=["hello","hai","python","apple","eagle"]
for vowel in vowels:
    for word in words:
        if word.startswith(vowel):
            print(word)
