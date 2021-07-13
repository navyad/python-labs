class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Person:
    def __init__(self, name, address):
        self.falls_ill = Event()
        self.falls_sick = Event()

    def catch_a_cold(self):
        print("person catches cold")
        self.falls_ill(self.name, self.address)

    def got_sick(self):
        print("person got sick")
        self.falls_sick(self.name, self.address)


def call_doctor(name, address):
    print(f'A doctor has been called to {address}')

def call_sick_doctor(name, address):
    print(f'A SICK doctor has been called to {address}')

if __name__ == '__main__':
    person = Person('Sherlock', '221B Baker St')
    person.falls_ill.append(call_doctor)
    person.catch_a_cold()

    person.falls_sick.append(call_sick_doctor)
    person.got_sick()
    # # and you can remove subscriptions too
    # person.falls_ill.remove(call_doctor)
    # person.catch_a_cold()