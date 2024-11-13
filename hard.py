'''

Here will define a class, OurDict, which will be an implementation of a dictionary
we will explicitly use a list for keys and a list for values, we will assume that they are the
same length and that the key at index, n, corresponds to the value at index n.

Implement it and add functionality for the given functions

'''

class OurDict():

    def __init__(keys, values):
        # TODO initializes self.keys and self.values using two given lists
        pass

    def add(self, key, value):
        # TODO adds a key value pair to our dict.
        # This should handle duplicates
        pass

    def remove(self, value):
        # TODO removes a pair with given value from the dict (i.e. self.remove(val) would remove {exkey: val} from the dict)
        pass

    def print(self):
        # TODO prints out OurDict in a similar format to the default python dict (i.e. {key1: val1, key2: val2, ...})
        pass

    def get(self, key):
        # TODO gets the value associated with the given key
        pass


# Some tests

our_dict = OurDict(["a","b","c"], [1,2,3])
our_dict.add("d", 4)
our_dict.print()
our_dict.remove(2)
our_dict.print()
our_dict.get("c")
our_dict.get("b")

# TODO write more test cases to make sure it works