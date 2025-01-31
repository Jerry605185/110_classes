'''

Create a new class verboseInt which will inherit all of the behavior of an integer except that the __str__() function is overidden
such that if the number is between -99 and 99 when printed it will print the value of the number in english. 
You also do not need to handle the teens values (11-19)

i.e. 5 would print "five" and 82 would print as "Eighty two"


'''

# Supplied for convenience
tens = {0:"", 2:"Twenty",3:"Thirty", 4:"Forty", 5:"Fifty", 6:"Sixty", 7:"Seventy", 8:"Eighty",9:"Ninety"}
ones = {0:"", 1: "one", 2:"two",3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight",9:"nine"}

class verboseInt(int):

    def __str__(self):
        # TODO redefine this so it prints how we want
        number = abs(self)
        word = ""
        if(0 < self < 10):
            word = ones[number]
        elif(-10 < self < 0):
            word = "negative " + ones[number]
        elif(self > 10):
            word = tens[number // 10] + " " + ones[number % 10]
        elif(self<-10):
            word = "negative " + tens[number // 10] + " " + ones[number % 10]
        return word
        pass

for val in [23, 8, 99, -20, 0, "5"]:
    myint = verboseInt(val)
    print(myint)
