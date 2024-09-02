# source_word="listen"
# target_word="silent"
# srt_source_word=sorted(source_word)
# srt_target_word=sorted(target_word)
# print(srt_source_word==srt_target_word)

def anagram(souce_word,target_word):
    return sorted(souce_word)==sorted(target_word)
print(anagram("silent","listen"))