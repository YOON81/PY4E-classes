x = 3
y = 10

if x < 10:
    print('Small')

# Alternative execution
if x%2 == 0 :
    print('x is even')
else:
    print('x is odd')

# Chained conditionals
if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')


# Nested conditionals
if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')


# simplify nested conditional statement
if 0 < x:
    if x < 10:
        print('x is a positive single-digit number.')

# simplify nested conditional statement and pass both conditionals
if 0 < x and x < 10:
    print('x is a positive single-digit number.')


