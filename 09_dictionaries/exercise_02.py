# Exercise 2: Write a program that categorizes each mail message by which day of
# the week the commit was done. To do this look for lines that start with "From",
# then look for the third word and keep a running count of each of the days of
# the week. At the end of the program print out the contents of your dictionary
# (order does not matter).
fname = input('Enter a file name: ')  # mbox-short.txt
if len(fname) < 1 : fname = 'mbox-short.txt'

try:
    fhand = open(fname)
except:
    print('Check the name again.')
    exit()


date = dict()
for line in fhand:
    line = line.rstrip()
    info = line.split()
    if len(info) < 3 or info[0] != 'From':
        continue
    else:
        #print(info[2])
        if info[2] not in date:
            date[info[2]] = 1
        else:
            date[info[2]] += 1

print(date)
