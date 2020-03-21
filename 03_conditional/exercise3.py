# Exercise 3: Write a program to prompt for a score between 0.0 and 1.0.
# If the score is out of range, print an error message.
# If the score is between 0.0 and 1.0, print a grade using the following table:
# ** 잘 된 코드 같음!! 기쁘다 **

score = input("Please enter score between 0.0 and 1.0 : \n")
try:
    score = float(score)
    if score > 1.0:
        print('Please check the input score!')
    elif score >= 0.9:
        print('Grade : A')
    elif score >= 0.8:
        print('Grade : B')
    elif score >= 0.7:
        print('Grade : C')
    elif score >= 0.6:
        print('Grade : D')
    else:
        print('Grade : F')

except ValueError:
    print("Bad input, Please retry it!")
