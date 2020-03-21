# List methods
t = ['a', 'b', 'c']
t.append('d')
print(t)

t2 = ['e', 'f']
t.extend(t2)
print(t)

t3 = ['d', 'f', 'c', 'a', 'b', 'e']
t3.sort()
print(t3)


# Deleting element
t3 = ['d', 'f', 'c', 'a', 'b', 'e']
x = t3.pop(1)
print(t3)
print(x)


t = ['a', 'b', 'c']
del t[1]
print(t)

t.remove('c')
print(t)


t = ['a', 'b', 'c', 'd', 'e', 'f']
del t[1:5]
print(t)


# Lists and functions
# max(), len() etc. work with lists of strings and other types that can be comparable.
# sum() only works when the list elements are numbers.
nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))



numlist = list()
while (True):
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    value = float(inp)
    numlist.append(value)
    # print(numlist)
average = sum(numlist) / len(numlist)
print('Average:', average)


# Lists and definite loops - best pals
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy new year', friend)


# Lists and strings
s = 'spam'
t = list(s)
print(t)


s = 'pinging for the fjords'
t = s.split()
print(t)
print(t[2])


s = 'spam-spam-spam'
delimiter = '-'
t = s.split(delimiter)
print(t)


m = ['pining', 'for', 'the', 'fjords']
delimiter = ' '
k = delimiter.join(m)
print(k)


# Parsing lines
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    print(words[2])




