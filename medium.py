'''

Here we are creating a class Dog which is going to be initialized with some given parameters, breed, color, size, and a boolean isloud
The initialization is taken care of here, but the functions still need to be completed

'''

class Dog():

    # When we construct a Dog object given parameters it will be initialized here
    def __init__(self, breed, color, size, isloud):
        self.breed = breed
        self.color = color
        self.size = size
        self.isloud = isloud

    def large(self):
        # TODO returns a boolean for if the size of the dog is >= 10
        pass

    def get_stats(self):
        # TODO prints out the stats of the dog in a human-legible way
        pass

    def speak(self):
        # prints "woof" if the dog is not large and loud == False, "Woof" if it is large or loud
        # and "WOOOF" if it is large and loud
        pass



# SOME TESTS TO CHECK YOUR CODE:
# ---------------------------------------------------------------------------------------
# Initializing a dog, basil, using some set attributes
basil = Dog(breed="Golden Doodle", color="Golden", size=15, isloud=False)

print(basil.large())

basil.get_stats()

basil.speak()

# Change an attribute of basil directly
basil.isloud=True

# Check it changed
basil.get_stats()

# See if speak changes accordingly
basil.speak()

# ---------------------------------------------------------------------------------------

# TODO Define your own dog and do a couple tests:
# ---------------------------------------------------------------------------------------




# ---------------------------------------------------------------------------------------