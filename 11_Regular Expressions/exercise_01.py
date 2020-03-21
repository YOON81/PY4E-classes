# Exercise 1: Write a simple program to simulate the operation of the grep command on Unix.
# Ask the user to enter a regular expression and count the number of lines that matched the
# regular expression:
#$ python grep.py
#Enter a regular expression: ^Author
#mbox.txt had 1798 lines that matched ^Author

#$ python grep.py
#Enter a regular expression: ^X-
#mbox.txt had 14368 lines that matched ^X-

#$ python grep.py
#Enter a regular expression: java$
#mbox.txt had 4175 lines that matched java$

import re
hand = open('mbox.txt')
inp = input('Enter a regular expression: ')  # Enter one of them : ^Author /  ^X-  /  java$
count = 0
for line in hand:
    line = line.rstrip()
    x = re.findall(inp, line)
    if len(x) > 0:
        count += 1
print('mbox.txt had', count, 'lines that matched', inp)
# mbox.txt had 1798 lines that matched ^Author
# mbox.txt had 14368 lines that matched ^X-
# mbox.txt had 4218 lines that matched java$
