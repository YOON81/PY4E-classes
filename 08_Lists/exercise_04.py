# Good job !! 힘내자!
inp = input('Enter file: ')

try:
    fhand = open(inp)

except:
    print('Can not be opened', inp)
    exit()

mlist = list()
for line in fhand:
    word = line.split()
    for element in word:
        if element not in mlist:
            mlist.append(element)
            mlist.sort()
print(mlist)

