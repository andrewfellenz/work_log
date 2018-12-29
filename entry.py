from datetime import date
from menu import Menu


class Entry():
    def __init__(self, order=None, date=None, task=None, duration=None, notes=None, deleted=False):
        self.order = order
        self.date = date
        self.task = task
        self.duration = duration
        self.notes = notes
        self.deleted = deleted
        self.keys = ('date', 'task', 'duration', 'notes')

    def __str__(self):
        info = f"""
Date: {self.date}
Task performed: {self.task}
Time spent on task: {self.duration}
Notes: {self.notes}
"""
        return info

    def __iter__(self):
        return self.keys
    
    @property
    def day(self):
        return int(self.date[3:5])

    @property
    def month(self):
        return int(self.date[0:2])

    @property
    def year(self):
        return int(self.date[6:])

    @property
    def realdate(self):
        return datetime.date(self.year, self.month, self.day)

        
    @classmethod
    def enter(cls):
        new_entry = cls(
            date = input('Please enter a date in MM/DD/YYYY format: '),
            task = input('Please enter what task you were working on: '),
            duration = input('Please enter how much time was spent on this task: '),
            notes = input('Please enter any additional notes: ')
            # order = to be determined
            )
        return new_entry
    

    @classmethod
    def recollect(cls, data):
        # collect previous JSON date
        entry = Entry()
        entry.date = data['date']
        entry.task = data['task']
        entry.duration = data['duration']
        entry.notes = data['notes']
        entry.order = data['order']
        return entry


    def edit(self, delete=False):
        if delete:
            self.deleted = True
        else:
            Menu(*self.keys).show()


if __name__ == '__main__':
    pass
