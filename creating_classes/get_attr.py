"""how to get attributes in classes"""


class Dog: 
    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name 
        self.age = age


dog1 = Dog('Doxie', 'Orange', 3)
dog2 = Dog('Poodle', 'Rex', 5)
dog3 = Dog('Golden Retriver', 'Chance', 1)

# print(dog1, 'this gives a location within memory')
# print(dog1.breed, dog1.name, dog1.age, 'you do not want to do this')

"want to create a new function the [str function]"

class Dog: 
    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name 
        self.age = age

    def __str__(self):
        return '\nName of Dog: ' +  self.name + '\nBreed: ' + self.breed + '\nAge:' + str(self.age)

dog1 = Dog('Doxie', 'Orange', 3)
print(dog1, '\now you do not get the memory location')