class Employee:
    def compute_salary(self):
        pass
    def give_raise(self):
        pass
    def promote(self):
        pass
    def retire(self):
        pass


"""
imagine that engineers get paid differently than all the other engineers at a company,you can by pass the behavior by defining a class for engineer"""

class Engineer(Employee):
    def compute_salary(self):
        return super().compute_salary()


""" superclasses are listed in parentheses in a class header

when you ask for the employee's salaries, they will be computed according to the classes from which the objects were made, due to the principles of the inheritance search"""