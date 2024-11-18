class Animal():

    def __init__(me, size, color):
        me.size = size
        me.color = color
    
    def print_size(self):
        print(self.size)
    
    def speak(self):
        print("I am an animal!")


class Dog(Animal):

    def __init__(self, size, color, breed):
        super().__init__(size, color) # Note self is not passed
        self.breed = breed
    
    def speak(self):
        print("I am a Dog!")

class Cat(Animal):

    def __init__(self, size, color):
        super().__init__(size, color) # Note self is not passed
        self.isViolent = True
    
    def speak(self):
        print("I am a Cat!")

Gunther = Animal(5, "Black and White")
Basil = Dog(20, "Golden", "Golden Doodle")
Elby = Cat(10, "Black")

Gunther.speak()
Basil.speak()
Elby.speak()

Gunther.print_size()
Basil.print_size()
Elby.print_size()
