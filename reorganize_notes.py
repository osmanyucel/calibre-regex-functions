import re
from calibre.gui2.tweak_book import current_container
from calibre.gui2.tweak_book.boss import get_boss
from calibre.ebooks.oeb.polish.container import OEB_DOCS


def replace(match, number, file_name, metadata, dictionaries, data, functions, *args, **kwargs):
    get_boss().commit_all_editors_to_container()
    get_boss().apply_container_update_to_gui()    
    notes = list()
    item_list = [x for x in current_container().mime_map.items() if x[1] in OEB_DOCS]
    item_list.sort()
    for name, mt in item_list:
        html = current_container().raw_data(name)
        notes_in_text = re.findall(r'<a href="notes[.]htm#n([0-9]*)"(.*?)</a>', html)
        for a in notes_in_text:
            notes.append((str(len(notes) + 1), a[0], a[0] + "xx"))
    for a in notes:
        change_note_numbers(a[1], a[2])
    for a in notes:
        change_note_numbers(a[2], a[0])
    reorder_notes()     
    return match.group()


def change_note_numbers(from_val, to_val):
        for name, mt in current_container().mime_map.items():
            if mt in OEB_DOCS:
                html = current_container().raw_data(name)
                old_ref = '<sup><a href="notes.htm#n{0}" id="n{0}d">[{0}]</a></sup>'.format(from_val)
                new_ref = '<sup><a href="notes.htm#n{0}" id="n{0}d">[{0}]</a></sup>'.format(to_val)
                old_note = '#n{0}d" id="n{0}">{0}</a>'.format(from_val)
                new_note = '#n{0}d" id="n{0}">{0}</a>'.format(to_val)
                html = html.replace(old_ref, new_ref)
                html = html.replace(old_note, new_note)
                current_container().open(name, 'wb').write(html.encode(encoding='UTF-8'))
                current_container().dirty(name)

    
def reorder_notes():
        html = current_container().raw_data('notes.htm')
        notes_in_text = re.findall(r'(<div><a href(.*?)id="n([0-9]+)(.|\s)*?</div>)', html)
        notes_in_text.sort(key=lambda y: int(y[2]))
        result = "<body>\n<h2>Notlar</h2>\n"
        for note in notes_in_text:
            result = result + "\n" + note[0]
        result = result + "\n" + "</body>"
        html = re.sub('<body>(.|\s)*</body>', result, html)
        current_container().open('notes.htm', 'wb').write(html.encode(encoding='UTF-8'))
        current_container().dirty('notes.htm')
