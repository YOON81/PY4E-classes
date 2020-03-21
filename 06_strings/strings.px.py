# len()
fruit = 'banana'
length = len(fruit)
last_letter = fruit[length - 1]
print(last_letter)


# Treversal through a string with a loop
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

# 위와 같은 방법으로 while 대신 for 이용하면
for char in fruit:
    print(char)


# String slices
s = 'Monty python'
print(s[:5])
print(s[6:])

print(fruit[:3])
print(fruit[3:])
print(fruit[:])


# Strings are immutable
# can't change an existing string. The best you can do is
# create a new string that is a variation on the original.
greeting = 'Hello world!'
new_greeting = 'J' + greeting[1:]
print(new_greeting)

# Looping and counting
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)


# String comparison
if word == 'banana':
    print('All right, bananas.')

if word < 'banana':
    print('Your word,' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word,' + word + ', comes after banana.')
else:
    print('All right, bananas.')


new_word = word.upper()
print(new_word)

index = word.find('a')
print(index)

line = '  Here we go   '
print(line.strip())

line = 'Have a nice day!'
print(line.startswith('Have'))  # True
print(line.startswith('h'))  # False
print(line.lower().startswith('h'))  # True


# Debugging
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
    if len(line) > 0 and line[0] == '#':
        continue
print('Done!')






