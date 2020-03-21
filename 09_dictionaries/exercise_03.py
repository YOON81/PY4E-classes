# Exercise 3: Write a program to read through a mail log, build a histogram using a
# dictionary to count how many messages have come from each email address, and print
# the dictionary.
fname = input('Enter a file name: ')  # mbox-short.txt
if len(fname) < 1 : fname = 'mbox-short.txt'

try:
    fhand = open(fname)
except:
    print('Check the name again.')
    exit()

emailist = dict()
for line in fhand:
    line = line.rstrip()
    word = line.split()
    if len(word) < 3 or word[0] != 'From':
        continue
    else:
        if word[1] not in emailist:
            emailist[word[1]] = 1
        else:
            emailist[word[1]] += 1

print(emailist)
