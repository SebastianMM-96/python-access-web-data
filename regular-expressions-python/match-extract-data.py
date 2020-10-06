import re

x = 'My 2 favorite numbers are 19 and 42'
# Regex
y = re.findall('[0-9]+', x)
print(y)