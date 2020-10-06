import re
x = 'From: Using the: character'
# Regex
y = re.findall('^F.+?:', x)
print(y)