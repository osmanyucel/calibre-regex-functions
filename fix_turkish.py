pairs = {
'i':'ı','I':'İ',
'c':'ç','C':'Ç',
's':'ş','S':'Ş',
'o':'ö','O':'Ö',
'u':'ü','U':'Ü',
'g':'ğ','G':'Ğ'
}


def replace(match, number, file_name, metadata, dictionaries, data, functions, *args, **kwargs):
    if dictionaries.recognized(match.group()):
        return match.group()
    return pick_best_result((match.group(),500), check_word(str(match.group()), 0, 0, dictionaries))[0]


def check_word(word, index, changed, dictionaries):
    if index>=len(word):
        if dictionaries.recognized(word):
            return word, changed
        else:
            return word, 9999
    result = check_word(word, index+1, changed, dictionaries)
    if word[index] in pairs:
        other_result = check_word(change_one_letter(word, index, pairs[word[index]]), index+1, changed+1, dictionaries)
        return pick_best_result(result, other_result)
    return result
        
        
def change_one_letter(word, index, new_val):
    s = list(word)
    s[index] = new_val
    return "".join(s) 


def pick_best_result(result1, result2):
    return result1 if result1[1] < result2[1] else result2
