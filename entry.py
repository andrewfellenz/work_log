from datetime import date
from menu_builder import Menu

class Entry():
    def __init__(self, order=None, date=None, task=None, duration=None, notes=None, deleted=False):
        self.order = order
        self.date = date
        self.task = task
        self.duration = duration
        self.notes = notes
        self.deleted = deleted
        self.keys = ('Date', 'Task', 'Duration', 'Notes')


    @classmethod
    def enter(cls):
        new_entry = cls(
            date = input('Please enter a date in MM/DD/YYYY format: '),
            task = input('Please enter what task you were working on: '),
            duration = input('Please enter how much time was spent on this task: '),
            notes = input('Please enter any additional notes: ')
            )
        return new_entry

    def edit(self, delete=False):
        if delete:
            self.deleted = True
        else:
            Menu(*self.keys).show()

e = Entry.enter()
