# Exercise 1: Revise a previous program as follows: Read and parse the "From" lines and
# pull out the addresses from the line. Count the number of messages from each person using
# a dictionary.
# After all the data has been read, print the person with the most commits by creating a
# list of (count, email) tuples from the dictionary. Then sort the list in reverse order
# and print out the person who has the most commits.

fhand = open('mbox.txt')

counts = dict()
for line in fhand:
    if line.startswith('From '):
        line = line.rstrip()
        emails = line.split()
        counts[emails[1]] = counts.get(emails[1], 0) + 1

lis = list()
for key, val in counts.items():  # tuple 로 바꾸는 작업임!
    newtup = (val, key)
    lis.append(newtup)

lis = sorted(lis, reverse=True)

for val, key in lis[:1]:
    print(key, val)  # zqian@umich.edu 195 가 나옴















