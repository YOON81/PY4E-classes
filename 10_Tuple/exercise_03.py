# Exercise 3: Write a program that reads a file and prints the letters in decreasing order
# of frequency. Your program should convert all the input to lower case and only count the
# letters a-z. Your program should not count spaces, digits, punctuation, or anything other
# than the letters a-z. Find text samples from several different languages and see how letter
# frequency varies between languages. Compare your results with the tables at
# https://wikipedia.org/wiki/Letter_frequencies.

inp = input('Enter a file name: ')  # romeo.txt
if len(inp) < 1 :
    inp = 'romeo.txt'
try:
    hand = open(inp)
except:
    print('Check the name of the file!')
    exit()

alpha = dict()
for line in hand:
    line = line.lower()
    t = tuple(line)
    alpha[t] = alpha.get(t, 0) + 1
print(alpha)
