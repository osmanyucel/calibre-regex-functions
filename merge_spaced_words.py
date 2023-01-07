# \p{L}(\p{L}|\s|[’]){5,35}(\W)
from functools import lru_cache
persistent_data = {"best_score" : -10000000000, "best_string":""}

 
def score(words, out):
    scorey = 0;
    for word in out.split(" "):
        scorey = scorey + (len(word)*len(word))
        if not words.recognized(word):
            scorey = scorey - 100
    return scorey

@lru_cache(maxsize = 100000)   
def wordBreak(words, word, out=''):
    if not word:
        scorey = score(words, out)
        if persistent_data["best_score"] < scorey:
            persistent_data["best_score"] = scorey
            persistent_data["best_string"] = out
        return
    for i in range(1, len(word) + 1):
        prefix = word[:i]
        if words.recognized(prefix) or len(prefix) ==1:
            wordBreak(words, word[i:], out + ' ' + prefix)


def replace(match, number, file_name, metadata, dictionaries, data, functions, *args, **kwargs):
    persistent_data["best_score"] = -10000000000
    persistent_data["best_string"] = ""
    wordBreak(dictionaries, match.group().replace(" ",""))
    if match.group(2) == " ":
        return persistent_data["best_string"] +" "
    else:
        return persistent_data["best_string"]
