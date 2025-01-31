# Authors : Jerry Chen
# Emails : yanzhechen@umass.edu
# Spire IDs : 34835664
def print_stars_to_file(n):
    with open(f"stars_{n}.txt","w") as file:
        for i in range(1,n+1):
            spaces = n-i
            stars = 2*i - 1
            file.write(" "*spaces + "*"*stars + "\n")
def calc_avg_from_file():
    with open("grades.txt","r") as file:
        text = file.read()
        text_list = text.split("\n")
        sum = 0
        counter = 0
        for num in text_list:
            sum += float(num)
            counter += 1
        return sum/counter
