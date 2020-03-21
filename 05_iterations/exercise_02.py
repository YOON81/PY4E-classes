# Exercise 2: Write another program that prompts for a list of numbers as above
# and at the end prints out both the maximum and minimum of the numbers
# instead of the average.
num_sum = 0
count = 0
average = 0
largest = None
smallest = None
while True:
    num = input('Enter a number:')

    try:
        num = float(num)
        num_sum = num + num_sum
        count = count + 1
        average = num_sum / count
        if largest is None or num > largest:
            largest = num
        elif smallest is None or num < smallest:
            smallest = num
    except ValueError:
        if num == 'Done' or num == 'done':
            break
        else:
            print('Invalid input')
            continue
print('sum:', num_sum, 'count:', count, 'average:', average, 'largest:', largest, 'smallest:', smallest)
