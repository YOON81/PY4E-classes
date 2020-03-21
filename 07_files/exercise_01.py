# Exercise 1:
fname = input('Enter a file name: ')
fhand = open(fname)

for line in fhand:
    result = line.rstrip()
    print(result.upper())

