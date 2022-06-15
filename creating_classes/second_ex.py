"""Method Overriding && 


Method Overloading - what I will display here is a trick to get method overloading because python does not support it like other languages do 
but in essence what it is is ======> a way to not necessarily pass a variable and have it work still

"""

class Student:
    def __init__(self, m1, m2): 
        self.m1 = m1
        self.m2 = m2

    def sum(self, a, b, c):
        s = a + b + c
        return s

# s1 = Student(58,59)
# print(s1.sum(1,3))
# print(s1.sum(1,3,8))


"""Exception has occurred: TypeError
Student.sum() missing 3 required positional arguments: 'a', 'b', and 'c'
  File "/Users/albamolina/python_classes/creating_classes/second_ex.py", line 19, in <module>
    print(s1.sum())
    IT MEANS YOU MUST PASS IN THREE ARGUMENTS SINCE YOU DEFINED A,B,C INSIDE DEF SUM IF YOU DO NOT PASS EXACTLY THE AMT OF ARGS YOU PASSED IN THEN IT WOULD BREAK
    A TRICK YOU CAN USE IS """
class Student:
    def __init__(self, m1, m2): 
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None, b=None, c=None):
        s = a+b+c
        return s

# s1 = Student(58,59)
# print(s1.sum(5,9,2)) # respectively only works when passing 3 variables so you need to do more code


class Student:
    def __init__(self, m1, m2): 
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None, b=None, c=None):
        s = 0
        if 1!=None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s = a+b
        else:
            s = a
        return s

# s1 = Student(58,59)
# print(s1.sum(5,9,2)) #three args
# print(s1.sum(5,9))   # two args
# print(s1.sum(5))        # one arg 

"""or you can just pass *args"""

"""


NOW LETS TALK ABOUT METHOD OVERRIDING
Basically it says if you have two classes
parent, child"""

class A:
    def show(self):
        print('A in show')

class B:
    pass


# a1 = B()
# a1.show()


"""
Exception has occurred: AttributeError
'B' object has no attribute 'show'
  File "/Users/albamolina/python_classes/creating_classes/second_ex.py", line 80, in <module>
    a1.show()
    

    you get an error saying that class B has no show attr 
    that is because you did not pass in Class A to Class B
    to fix it: """

class A:
    def show(self):
        print('A in show')

class B(A):
    pass

# a1 = B()
# a1.show()


"""the moment you define a method inside 2nd class (child) with the same name, it takes that method instead of the one being passed into it"""

class A:
    def show(self):
        print('A in show')

class B(A):
    def show(self):
        print('B in show')


a1 = B()
a1.show()