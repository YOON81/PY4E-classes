t = tuple('lupins')
#print(t)  # ('l', 'u', 'p', 'i', 'n', 's')
#print(t[0])  # l
#print(t[1:3])  # ('u', 'p')
t = ('L',) + t[1:]  # 튜플의 요소를 수정 살 수 없다. 하지만 또 다른 하나의 튜플을 대체 할 수 있다 **
#print(t)  # ('L', 'u', 'p', 'i', 'n', 's')


# Comparing tuples
txt = 'but soft what light in youder window breaks'
words = txt.split()
t = list()
for word in words:
    t.append((len(word), word))

t.sort(reverse=True)

res = list()
for length, word in t:
    res.append(word)
#print(res)  # ['youder', 'window', 'breaks', 'light', 'what', 'soft', 'but', 'in']



# Tuple assignment
m = ['have', 'fun']
x = m[0]
y = m[1]
#print(x)  # have
#print(y)  # fun
(x, y) = m
# print(x, y)  # have fun


addr = 'monty@python.org'
uname, domain = addr.split('@')
#print(uname)  # monty
#print(domain)  # python.org



# Dictionaries and tuples
d = {'c':10, 'b':1, 'a':22}
t = list(d.items())
#print(t)  # [('c', 10), ('b', 1), ('a', 22)]
t.sort()
#print(t)  # [('a', 22), ('b', 1), ('c', 10)]
for key, val in list(d.items()):
    #print(val, key)  # 10 c
                     # 1 b
                     # 22 a



# Muliple assignment with dictionaries
# print out the contents of a dictionary sorted by the value stored in each key-value pair.
 new = {'a': 14, 'b': 10, 'c': 29}
lis = list()
for key, val in new.items():  # tuple 로 바꾸는 idiom  !
    lis.append((val, key))
#print(l)  # [(14, 'a'), (10, 'b'), (29, 'c')]
lis.sort(reverse=True)  # 거꾸로 정렬을 하는 방법 !
#print(l)  # [(29, 'c'), (14, 'a'), (10, 'b')]



# The Most Common Words
fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    line = line.lower()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.items():  # tuple 로 바꾸는 작업임!
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)  # 거꾸로 정렬 하는 작업

for val, key in lst[:5]:  # 거꾸로 정렬 된 것을 5 줄만 key와 value를 자리 바꿔 프린트 하는 작
    print(key, val)

#위의 short version
# print(sorted([(val, key) for key, val in counts.items()]))




