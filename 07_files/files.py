fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)

# Searching through a file
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)


# use .find() method
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1:  # if the string was not found.
        continue
    print(line)


# Letting the user choose the file name
fname = input('Enter the file name: \n')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)


# Using try, except, open
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject line in', fname)


# Writing files
fout = open('output.txt', 'w')
print(fout)
line1 = "this here's the wattle (second time),\n"

print(fout.write(line1))
fout.close()  #


# Debugging
s = '1 2\t 3\n :)\t 4 david'  # return character, represented \t
print(s)
print(repr(s))  # The built-in function repr can help.
# It takes any object as an argument and returns a string representation of
# the object. For strings, it represents whitespace characters with backslash
# sequences:
