import json
from entry import Entry
from menu import Menu

# This will be the file that controls the reading and writing
# of the entries
with open('data.json', 'r') as write_file:
    data = json.load(write_file)
    entries = [Entry.recollect(entry) for entry in data]
    for entry in entries:
        print(entry)

e = Menu(*entries[1].keys).show()


with open('output.json', 'w') as write_file:
    json.dump(entries, write_file, indent=4)
