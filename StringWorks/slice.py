name="akhil g krishan"
sliced_name=name[0:5]
sliced_name=name[0:]
sliced_name=name[:15]
sliced_name=name[::-1]
sliced_name=name[15:4:-1]
print(sliced_name)

def is_palindrome(word):
    
    rev_word=word[::-1]

    return word==rev_word

print(is_palindrome("malayalam"))