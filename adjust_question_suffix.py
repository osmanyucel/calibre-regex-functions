#(\b\w+\b) (\bmi\w+\b)
from calibre.spell import parse_lang_code
from qt.core import pyqtSignal

to_AI={
"misin": "mısın",
"miyim": "mıyım",
"midir": "mıdır",
"mi": "mı",
}

to_OU = {
"musun": "müsün",
"muyum": "müyüm",
"mudur": "müdür",
"mu": "mü",
}


suffices = {
"a":to_AI,
"ı":to_AI,
"ö":to_OU,
"ü":to_OU,
}

def replace(match, number, file_name, metadata, dictionaries, data, functions, *args, **kwargs):
    word = match.group(1)
    suffix = match.group(2)
    vowel = find_last_vowel(word)
    if vowel in suffices and suffix in suffices[vowel]:
        return word+" "+suffices[vowel][suffix]
    return match.group()


def find_last_vowel(word):
    vowels = ('a','e','ı','i','o','ö','u','ü')
    for c in reversed(word):
        if c in vowels:
            return c
