'''

Implement the class Counter below, all it will do is hold an attribute "count" which it can modify or print

'''

class Counter():
    count = 0

    def print_count(self):
        # TODO prints out the current value of count
        pass

    def increase_count(self, amount):
        # TODO increase the value of count by amount
        pass

    def double_count(self):
        # TODO doubles the count attribute
        pass


counter1 = Counter()
counter2 = Counter()

counter1.increase_count(5)

counter2.count = 100
counter2.double_count()

counter1.print_count()
counter2.print_count()