import datetime
from menu import Menu


class Entry():
    def __init__(self, date=None, task=None, duration=None, notes=None, order=None, deleted=False):
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
        return self.key

    @property
    def output(self):
        return {
            'order': self.order,
            'date': self.date,
            'task': self.task,
            'duration': self.duration,
            'notes': self.notes
        }
    
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
        return datetime.datetime(self.year, self.month, self.day, 0, 0, 0, 0)

    @property
    def posix(self):
        return self.realdate.timestamp()
    
    @classmethod
    def orders(cls, *instances):
        all_posix = []
        for instance in instances:
            all_posix.append(instance.posix)
        all_posix.sort()
        for instance in instances:
            instance.order = all_posix.index(instance.posix) + 1
        # I learned aboute lambda from a stack exchange post:
        # https://stackoverflow.com/questions/403421/how-to-
        # sort-a-list-of-objects-based-on-an-attribute-of-
        # the-objects/48731059
        new_order = sorted(instances, key=lambda x: x.order)
        return new_order
                
        
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
    def recollect(cls, *instances):
        entries = [cls(
            instance['date'],
            instance['task'],
            instance['duration'],
            instance['notes'],
            instance['order']
        ) for instance in instances]
        return entries


    def edit(self, delete=False):
        if delete:
            self.deleted = True
        else:
            selection = Menu(*self.keys).show()
            what_to_change = "The original info is "\
            + "\"" + f"{getattr(self, selection)}" + "\","\
            + " what would you like to change it to? > "
            new_info = input(what_to_change)
            setattr(self, selection, new_info)
            return self


if __name__ == '__main__':
    pass
