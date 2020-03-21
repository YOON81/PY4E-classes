eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
vals = list(eng2sp.values())
#print('uno' in vals)  # True



# Dictionary as a set of counters
# get() : write if statement and loop more concisely.
word = 'brontosaurus'
d = dict()
for c in word:
    d[c] = d.get(c, 0) + 1  # 0 is default value.

#print(d)  # {'b': 1, 'r': 2, 'o': 2, 'n': 1, 't': 1, 's': 2, 'a': 1, 'u': 2}



# Dictionaries and files
fname = input('Enter the file name: ')  # romeo.txt
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1


#print(counts)



# Looping and dictionaries
counts = {'chuck': 1, 'annie': 42, 'jan': 100}
for key in counts:
    if counts[key] > 10:
        #print(key, counts[key])



counts = {'chuck': 1, 'annie': 42, 'jan': 100}
lst = list(counts.keys())  # ['chuck', 'annie', 'jan']
print(lst)
lst.sort()
for key in lst:
    #print(key, counts[key])  # annie 42
                             # chuck 1
                             # jan 100



# Advanced text parsing
import string
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('Wrong file name')
    exit()

counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)



# Counting Word Frequency Using a Dictionary ** 매우 중요함 ! **
fname = input('Enter File: ')
if len(fname) < 1 : fname = 'mbox-short.txt'  # 디폴트(그냥 엔터만 치면)로 이 파일이 열리
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        di[w] = di.get(w, 0) + 1  # idiom: retrieve/ creat/ update counter
        #print(w, di[w])
#print(di)

# now we want to find the most common word
largest = -1
theword = None
for k, v in di.items():  # idiom
    if v > largest:
        largest = v
        theword = k  # capture/ remember the word was the largest

print('Largest', k, v)  # 원하는 값이 안나오는데 !!

