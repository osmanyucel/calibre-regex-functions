import re

def replace(match, number, file_name, metadata, dictionaries, data, functions, *args, **kwargs):
    strg = match.group()
    return re.sub(r"</p>\s*<p>", " ", strg)
    
