import re
from calibre.gui2.tweak_book import current_container
from calibre.gui2.tweak_book.boss import get_boss


def create_reference(note_num):
    return "<sup><a href=\"notes.htm#n{note_num}\" id=\"n{note_num}d\">[{note_num}]</a></sup>".format(note_num=note_num)


def create_footnote(file_name, note_num, content):
    return "<div><a href=\"{file_name}#n{note_num}d\" id=\"n{note_num}\">{note_num}</a><p> {content}</p></div>".format(
        file_name=file_name, note_num=note_num, content=content)


def find_next_note_num():
    last_note_num = 0
    html = current_container().raw_data("notes.htm")
    for match in re.finditer(r"([0-9]+)</a>", html):
        last_note_num = max(last_note_num, int(match.group(1)))
    return last_note_num + 1

def append_note(note):
    html = re.sub('</body>', note + "\n</body>", current_container().raw_data("notes.htm"))
    current_container().open("notes.htm", "w").write(html)
    current_container().dirty("notes.htm")
    current_container().commit()
    
def create_notes_file_if_missing(title):
    if current_container().exists("notes.htm"):
       return
    
    html = """<?xml version='1.0' encoding='utf-8'?>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>{}</title>
    <link type="text/css" rel="stylesheet" href="page_styles.css"/>
    <link type="text/css" rel="stylesheet" href="stylesheet.css"/>
</head>
<body>
    <h2>Notlar</h2>    
</body>
</html>
        """.format(title)
    current_container().add_file("notes.htm", html.encode("UTF-16"), media_type="application/xhtml+xml")
    
def replace(match, number, file_name, metadata, dictionaries, data, functions, *args, **kwargs):
    get_boss().commit_all_editors_to_container()
    create_notes_file_if_missing(metadata.title)
    note_num = find_next_note_num()
    append_note(create_footnote(file_name, note_num, match.group(1)))
    get_boss().apply_container_update_to_gui()
    

    return create_reference(note_num)
