fname = input('Enter a file name: ')  # mbox-short.txt

try:
    fhand = open(fname)

except:
    print('Enter a wrong file name.')
    exit()

count = 0
for line in fhand:
    line = line.rstrip()
    email = line.split()
    if len(email) < 3 or email[0] != 'From':
        continue
    count = count + 1
    print(email[1])

print("There were", count, "lines in the file with From as the first word")
# There were 27 lines in the file with From as the first word