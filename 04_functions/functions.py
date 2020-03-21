# Math functions
import math

degree = 45
radians = degree / 360.0 * 2 * math.pi
print(math.sin(radians))

print(math.sqrt(2) / 2.0)

# Random numbers
import random

for i in range(3):
    x = random.random()
    print(x)

# The function randint takes the parameters low and high,
# and returns an integer between low and high (including both)
print(random.randint(5, 10))
print(random.randint(5, 10))

# Choice
t = [1, 2, 3, 4, 5]
print(random.choice(t))
print(random.choice(t))


# Adding new functions (define function)
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')


print_lyrics()


# Use the defined function inside another function
def repeat_lyrics():
    print_lyrics()
    print_lyrics()


repeat_lyrics()


# Parameters and arguments
def print_twice(bruce):
    print(bruce)
    print(bruce)


print_twice('spam ' * 4)
print_twice(17)

import math

print_twice(math.cos(math.pi))

michael = 'Eric, the half a bee.'
print_twice(michael)


# Fruitful functions and void functions (중요함!)
# To return a result from a function, use the return statement in the function.
def addtwo(a, b):
    added = a + b
    return added


x = addtwo(3, 5)

print(x)
