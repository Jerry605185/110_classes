# Authors : Jerry Chen
# Emails : yanzhechen@umass.edu
# Spire IDs : 34835664
def count_words(my_tuple):
    some_dict = {}
    for word in my_tuple:
        if word in some_dict:
            some_dict[word] += 1
        else:
            some_dict[word] = 1
    return some_dict
def average_prices(my_tuple1):
    some_dict1 = {}
    count = {}
    average = {}
    for name, prices in my_tuple1:
        if name in some_dict1:
            some_dict1[name] += prices
            count[name] += 1
        else:
            some_dict1[name] = prices
            count[name] = 1
    for item in some_dict1:
        average.update({item:some_dict1[item]/count[item]})
    return average
prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
print(average_prices(prices))
