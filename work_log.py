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


# WORKING NOTES: entries misisng fields are currently null


import json
# Imports the main class used to control entries
from entry import Entry
# Imports the menu functions 
from menu import Menu


with open('logs.json', 'r') as data:
    file_check = data.read(1)
    if not file_check:
        entries = []
    else:
        data.seek(0)
        new_data = json.load(data)
        entries = Entry.recollect(*new_data)


# This is a temporary function for testing purposes
def CallClose():
    output = [entry.output for entry in Entry.orders(*entries)]
    with open('logs.json', 'w') as write_file:
        json.dump(output, write_file, indent=2)
