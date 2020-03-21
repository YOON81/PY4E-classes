# Exercise 2:
# 일단은 좋은 코드로 보임 ! **
fname = input("Enter file name: ")
fh = open(fname)
count = 0
plus = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        colon = line.find(':')
        num = line[colon+1:]
        value = float(num)
        plus = plus + value
        count = count + 1
        average = plus / count


print('Average spam confidence:', average)

