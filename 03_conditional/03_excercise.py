# 01_ Exercise :
# pay computation to give the employee 1.5 times the hourly rate
# for hours worked above 40 hours.
# ** 잘 된 코드 같음!! 기쁘다 **

hours = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))
try:
    if hours <= 40:
        pay = (hours * rate)
        print(pay)
    else:
        pay = (40 * rate) + (((hours - 40) * rate) * 1.5)
        print(pay)

except ValueError:
    print('Error, Please enter numeric input')






