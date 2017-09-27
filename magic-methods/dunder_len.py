from itertools import count


class Ticket(object):
    """
    implemented __len__ to return number of instances
    """
    active_counts = count(1)
    deleted_counts = count(0)

    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls, *args, **kwargs)
        return obj

    def __init__(self):
        self.total_tickets = next(self.active_counts)

    def __len__(self):
        return self.total_tickets

obj_1 = Ticket()
print len(obj_1)
obj_2 = Ticket()
print len(obj_2)
obj_3 = Ticket()
print len(obj_3)
