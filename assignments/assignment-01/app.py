import re

# get the file
get_file = open('regex_sum_1015320.txt')

list_ = list()

for lines in get_file:
    # regex
    regex = re.findall('[0-9]+', lines)
    # summ all
    list_ = list_ + regex

sum_ = 0
for aux in list_:
    sum_ = sum_ + int(aux)

# get result
print(sum_)