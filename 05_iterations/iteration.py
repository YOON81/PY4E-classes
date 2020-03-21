# Definite loops using : for
friends = ['David', 'Yoon', 'Chris']
for friend in friends:
    print('Happy New year:', friend)
print('done!')

# Loop pattern
# Count the number of items in the list:
count = 0
for intervar in [3, 39, 40, 5, 89, 17]:
    count = count + 1
print('Count:', count)

# The total of a set of numbers:
total = 0
for intervar in [3, 39, 40, 5, 89, 17]:
    total = total + intervar
print('Total: ', total)

# Maximum and minimum loops
largest = None
print('Before:', largest)
for intervar in [3, 39, 40, 5, 89, 17]:
    if largest is None or intervar > largest:
        largest = intervar
    print('Loop:', intervar, largest)
print('Largest:', largest)

smallest = None
print('Before:', smallest)
for intervar in [3, 39, 40, 5, 89, 17]:
    if smallest is None or intervar < smallest:
        smallest = intervar
    print('Loop:', intervar, smallest)
print('Smallest:', smallest)

# max() , min()
def min(values):
    smallest = None
    for value in values:
        if smallest is None or value < smallest:
            smallest = value
    return smallest
print(smallest)
