## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

# Dog is an animal
class Dog(Animal):
 
    def __init__(self, name):
# self has a name
        self.name = name

## Cat is an animal
class Cat(Animal):

    def __init__(self, name):
# self has a name
        self.name = name

## Person is an object
class Person(object):

    def __init__(self, name):
    #Person has some name
        self.name = name

    #Person has-a pet of some kind
        self.pet = None
 
# employee is a person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary

# Fish is an object
class Fish(object):
    pass

 # Salmon is a fish
class Salmon(Fish):
    pass

## Halibut is a fish
class Halibut(Fish):
    pass


# rover is-a Dog
rover = Dog("Rover")

# satan us a cat
satan = Cat("Satan")

# mary is a person
mary = Person("Mary")

# mary has a pet named satan
mary.pet = satan

#frank is an employee
frank = Employee("Frank", 120000)

# frank has a pet called rover
frank.pet = rover

# flipper is a fish
flipper = Fish()

# crouse has a salmon
crouse = Salmon()

# harry has a halibut
harry = Halibut()
