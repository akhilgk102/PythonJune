f=open("C:\\Users\\akhil\\Desktop\\PythonJune\\File_programs\\news.txt","r")

word_list=[w for words in f for w in words.rstrip("\n").split(" ")if w!=""]

word_count={w:word_list.count(w) for w in word_list}

def get_key(key):

    return word_count.get(key)

srt=sorted(word_count,key=get_key,reverse=True)

print(srt)
