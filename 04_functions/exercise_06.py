# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and
# create a function called computepay which takes two parameters (hours and rate).
# ** 첫번째 질문에 문자 입력했을 때 에러 메세지 뜨는 건 아직 해결 안됨 **
# ** 마지막 프린트문에 에러 뜸 ! **

hours = input('Enter Hours: ')
rate = input('Enter Rate: ')

try:
    hours = float(hours)
    rate = float(rate)
    def computepay(hours, rate):
        if hours <= 40:
            hours_pay = (hours * rate)
            return hours_pay
        else:
            hours_pay = (40 * rate) + (hours - 40) * rate * 1.5
            return hours_pay

except ValueError:
    print('Error, Please enter numeric input')

print(computepay(hours, rate))

