# Import needed modules

# Receive entries from users

# Information must include date, title of the task, time spent,
# -and general notes

# Entries must be searchable: find by date - find by time spent
# -find by exact search - find by pattern (regex)

# Any search option should present items to choose from
# -before any data is entered

# User should be presented with a menu to decide what to do

# They can search a previous task, enter a new task, etc...

# EXTRA CREDIT
# Menu has a quit option
# Entries can be deleted and every field can be edited
# Date RANGES are acceptable search tools
# Entries are displayed one at a time and there's a tool
# -that allows the user to page through entries.

import json
from entry import Entry
from menu import Menu

# This will be the file that controls the reading and writing
# of the entries
with open('data.json', 'r') as write_file:
    data = json.load(write_file)
    entries = Entry.recollect(*data)

output = [entry.output for entry in Entry.orders(*entries)]


with open('output.json', 'w') as write_file:
    json.dump(output, write_file, indent=2)


