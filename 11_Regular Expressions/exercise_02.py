# Exercise 2: Write a program to look for lines of the form: New Revision: 39772
# Extract the number from each of the lines using a regular expression and the findall()
# method. Compute the average of the numbers and print out the average as an integer.
import re
hand = open('mbox-short.txt')

total = 0
count = 0
for line in hand:
    line = line.rstrip()
    x = re.findall('^New Revision: ([0-9.]+)', line)
    if len(x) > 0:
        fx = float(x[0])
        count += 1
        total += fx

print(count)  # 27
print(total)  # 1073437.0
print(total/count)  # 39756.92592592593







