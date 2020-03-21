#Exercise 1: Write a program which repeatedly reads numbers until the user enters
# "done". Once "done" is entered, print out the total, count, and average of the
# numbers. If the user enters anything other than a number, detect their mistake
# using try and except and print an error message and skip to the next number.
num_sum = 0
count = 0
average = 0

while True:
    num = input('Enter a number:')

    try:
        num = float(num)
        num_sum = num + num_sum
        count = count + 1
        average = num_sum / count
    except ValueError:
        if num == 'Done' or num == 'done':
            break
        else:
            print('Invalid input')
            continue
print('sum:', num_sum, 'count:', count, 'average:', average)





