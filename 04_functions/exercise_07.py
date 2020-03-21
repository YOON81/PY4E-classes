# Exercise 7: Rewrite the grade program from the previous chapter using a
# function called computegrade that takes a score as its parameter and
# returns a grade as a string.
# ** 이유를 모르겠으나 완전 오작동!!! **

score = input("Please enter score between 0.0 and 1.0 : \n")
score = float()
try:
    def computegrade(score):
        if score > 1.0:
            return 'Please check the input score!'
        elif score >= 0.9:
            return 'Grade : A'
        elif score >= 0.8:
            return 'Grade : B'
        elif score >= 0.7:
            return 'Grade : C'
        elif score >= 0.6:
            return 'Grade : D'
        elif score < 0.6:
            return 'Grade : F'

except ValueError:
    print("Bad input!")

print(computegrade(score))
