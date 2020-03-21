# 5.2 Write a program that repeatedly prompts a user for integer numbers until
# the user enters 'done'. Once 'done' is entered, print out the largest and
# smallest of the numbers. If the user enters anything other than a valid number
# catch it with a try/except and put out an appropriate message and ignore the
# number. Enter 7, 2, bob, 10, and 4 and match the output below.
# https://stackoverflow.com/questions/31256648/beginner-python-code-issues/48087795
largest = None
smallest = None
while True:
    num = input('Enter a number:')
    if num == 'done':
        break
    try:
        num = int(num)
        if smallest is None or num < smallest:
            smallest = num
        elif largest is None or num > largest:
            largest = num

    except ValueError:
        print('Invalid input')
        continue
print('Maximun is', largest)
print('Minimun is', smallest)

# 100 점 !! **