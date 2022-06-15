

"""class based"""
class rec:
    pass

rec.name = 'bob'
rec.age = 40
rec.jobs = ['inst', 'gamer']

# print(rec.name)

class Person:
    def __init__(self, name, jobs, age=None):
        self.name = name
        self.jobs = jobs
        self.age = age

    def info(self):
        return (self.name, self.jobs)

rec1 = Person('Andy', ['gym instructor', 'manager'], 8)
rec2 = Person('Ollie', ['stay at home cat'], 1)

print(rec1.jobs, rec2.info())
# object.attribute