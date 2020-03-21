# Exercise 5: This program records the domain name (instead of the address) where the message
# was sent from instead of who the mail came from (i.e., the whole email address).
# At the end of the program, print out the contents of your dictionary.
fname = input('Enter file name; ')
if len(fname) < 1:
    fname = 'mbox-short.txt'

try:
    fhand = open(fname)

except:
    print('Check the file name.')
    exit()

domains = dict()
for line in fhand:
    line = line.rstrip()
    word = line.split()
    if line.startswith('From '):
        email = word[1]
        domain = email.split('@')
        domains[domain[1]] = domains.get(domain[1], 0) + 1
print([domains])





