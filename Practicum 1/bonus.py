'''
The OurList class will be our implementation of a list, it will take a list as an input to its constructor and will create an object 
with similar functionality that we will implement.

The basis of our class is that it will be a linked-list -- This means that each instance of the object will be linked to another instance (stored in self.next)
we can interate through our list by repeatedly going into the next element.
'''

class OurList():

    # When we call x = OurList(lst) it will run the code beneath
    def __init__(self, lst: list):
        # TODO initialize all of the necessary attributes using the given list, lst
        # An OurList object should have 2 attributes, self.value and self.next
        # self.next should either be another OurList object or None
        pass

    def append(self, elem):
        # TODO append a new element elem on to the end of the OurList object
        # Hint: you will have to iterate through OurList objects (self.next) and should only be changing
        # a self.next which is None to a new object.
        pass

    def length(self, elem):
        # TODO returns the length of the OurList object.
        pass

    def at(self, index):
        # TODO returns the value at the given index
        pass

    def insert(self, index, elem):
        # TODO inserts the given element at the given index
        pass

# TODO Write tests for each of the functions you have written