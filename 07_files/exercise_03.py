# Exercise 3:
# 잘 된 코드라는 생각이 듦 ! **

fname = input('Enter the file name:\n')
fhand = open(fname)
try:
    if fname == 'na na boo boo':
        print('Na Na Boo Boo To You - You have been punk\'d')

    else:
        fhand = open(fname)

except:
    print('File can not be opened:', fname)
    exit()

count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)
