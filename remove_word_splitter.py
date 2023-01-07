
def replace(match, number, file_name, metadata, dictionaries, data, functions, *args, **kwargs):
    new_word = match.group(1)+match.group(2)
    if dictionaries.recognized(new_word):
        return new_word
    return match.group()
    
