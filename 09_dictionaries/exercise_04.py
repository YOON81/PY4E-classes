# Exercise 4: Add code to the above program to figure out who has the most messages
# in the file. After all the data has been read and the dictionary has been created,
# look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum
# loops) to find who has the most messages and print how many messages the person has.

fname = input('Enter a file name: ')  # mbox-short.txt
if len(fname) < 1:
    fname = 'mbox-short.txt'

try:
    fhand = open(fname)
except:
    print('Check the name again.')
    exit()

emailist = dict()
for line in fhand:
    line = line.rstrip()
    word = line.split()
    if line.startswith('From '):
        emailist[word[1]] = emailist.get(word[1], 0) + 1

#print(emailist)

largest = 0
themail = None
for key, value in emailist.items():
    if largest == 0 or value > largest:
        largest = value
        themail = key
print('The most message is', themail, largest)  # The most message is cwen@iupui.edu 5

# good job Yoon!