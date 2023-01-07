import regex as re


def replace(match, number, file_name, metadata, dictionaries, data, functions, *args, **kwargs):
    result = '<ul>'
    result = result + match.group().replace("<p>","<li>").replace("</p>","</li>")
    result = result + '</ul>'
    return result
