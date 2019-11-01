"""Class
A class is a blueprint for the object.

We can think of class as an sketch of a parrot with labels. It contains all the details about the name, colors, size etc. Based on these descriptions, we can study about the parrot. Here, parrot is an object.

The example for class of parrot can be :"""
print("=============Parrot Class Prints:================")
class Parrot:
    #class Attributes
    species = 'bird'

    #instance Attribute
    def __init__(self, name, age):
        self.name= name
        self.age= age

    #instance methods
    def sing(self,song):
        return "{} sings {}".format(self.name,song)

    def dancing_parrot(self):
        return "{} is now a dancing parrot".format(self.name)


#Use That class
blue = Parrot("Blue", 10)
woo = Parrot("Woo",15)

#accessing the classes attributes
print("Blue is a {}".format(blue.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

#access the instance attributes

print("{} is {} years old".format(blue.name, blue.age))
print("{} is {} years old".format(woo.name, woo.age))
    
#call our instance methods
print(blue.sing("'ye-HAW'"))
print(blue.dancing_parrot())

print("=================Use Of Inheritance====================")
#==========================Use Of Inheritance Python======================++#
class Bird:
    def __init__(self):
        print("BIrd is ready to fly my guy")

    def who_am_I(self):
        print("is bird")

    def swim(self):
        print("swim faster bird")

#child class
class Penguin(Bird):
    
    def __init__(self):
        super().__init__()
        print("PENGUIN WILL NOT LOSE THE BATTLE")

    def who_am_I(self):
        print("I im penguin ^.^")

    def run(self):
        print("RUN PENGUIN. BECOME BEST BIRD")

penguinNation = Penguin()
penguinNation.who_am_I()
penguinNation.swim()
penguinNation.run()