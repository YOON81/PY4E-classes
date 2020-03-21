# Exercise 2: This program counts the distribution of the hour of the day for each of the
# messages. You can pull the hour from the "From" line by finding the time string and then
# splitting that string into parts using the colon character. Once you have accumulated the
# counts for each hour, print out the counts, one per line, sorted by hour as shown below.

fname = input('Enter file name: ')  # mbox-short.txt
if len(fname) < 1:
    fname = 'mbox-short.txt'

try:
    fhand = open(fname)

except:
    print('Wrong input!')
    exit()

hours = dict()
for line in fhand:
    if line.startswith('From '):
        hour = line.split()[5].split(':')[0]  # 모든게 함축된 코드
        hours[hour] = hours.get(hour, 0) + 1


for key, val in sorted(hours.items()):  # tuple 로 바꾸고 key 별로 정렬 시킴
    print(key, val)