from first_ex import FirstClass

class SecondClass(FirstClass):
    def display(self):
        print(FirstClass)

import first_ex
class SecondClass(first_ex.FirstClass):                                  # inherit setdata
    def display(self):
        print('current value = ', '%', self.data)


z = SecondClass()
z.setdata(42)
z.display()

print(first_ex, type(first_ex))





"""
when importing classes from a diff module
up top: 
import module_name

class SecondClass(first_ex.FirstClass):                                  # inherit setdata
    def display(self):
        print('current value = ', '%', self.data)



        or 
        from first_ex import FirstClass

class SecondClass(FirstClass):
    def display(self)
print(FirstClass)
"""