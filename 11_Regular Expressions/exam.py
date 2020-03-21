#Finding Numbers in a Haystack
#In this assignment you will read through and parse a file with text and numbers.
# You will extract all the numbers in the file and compute the sum of the numbers.
import re
handle = open("regex_sum_377290.txt")
numlist=list()
for line in handle :
    line = line.rstrip()
    stuff = re.findall('([0-9.]+)',line)
    for element in stuff :
        try :
            num = int(element)
            numlist.append(num)
        except :
            continue
print(sum(numlist))