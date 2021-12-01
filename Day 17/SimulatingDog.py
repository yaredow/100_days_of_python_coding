class Dog:
    """A simple attempt to model a dog"""


    def __init__(self, name, age):
        """Initialize the name and age attributes"""
        self.name = name
        self.age = age


    def sit(self):
        """Simulating a dog sitting"""
        print("{} is now sitting".format(self.name))


    def roll_over(self):
        """Simulating the dog rolling over"""
        print("{} rolled over".format(self.name))
    

    def attack(self):
        print("{} attacked your dog".format(self.name))

my_dog = Dog("Jack", 10)
print("My dog name is {} and it is {} years old".format(my_dog.name, my_dog.age))
my_dog.roll_over()
my_dog.sit()
my_dog.attack()