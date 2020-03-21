#Finding Numbers in a Haystack
#In this assignment you will read through and parse a file with text and numbers.
# You will extract all the numbers in the file and compute the sum of the numbers.
import re
handle = open('regex_sum_330187.txt')
numbers = 0
for line in handle:
    line = line.rstrip()
    numbers = numbers + sum(map(lambda x: int(x), re.findall('([0-9]+)', line)))

print(numbers)