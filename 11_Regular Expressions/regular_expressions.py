# Search for lines that contain 'From'
#import re
#hand = open('mbox-short.txt')
#for line in hand:
    #line = line.rstrip()
    #if re.search('^From:.+@', line):    # re.search('^ ~',) = line.startswith()와 같다.
        #print(line)                  # 그리 re.search() = line.find(와 같다



# Search for lines that have an at sign between characters  [a-zA-Z0-9]\S*@\S*[a-zA-Z]
#import re
#hand = open('mbox.txt')
#for line in hand:
    #line.rstrip()
    #x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
    #if len(x) > 0:
        #print(x)



#Combining searching and extracting
# Search for lines that start with 'X' followed by any non
# whitespace characters and ':'
# followed by a space and any number.
# The number can include a decimal.
#import re
#hand = open('mbox-short.txt')
#for line in hand:
#    line = line.rstrip()
#    x = re.findall('^X\S*: ([0-9.]+)', line)
#    if len(x) > 0:
#       print(x)



# Search for lines that start with 'Details: rev='
# followed by numbers and '.'
# Then print the number if it is greater than zero
#import re
#hand = open('mbox-short.txt')
#for line in hand:
#    line = line.rstrip()
#    x = re.findall('^Details:.*rev=([0-9.]+)', line)
#    if len(x) > 0:
#        print(x)



# Search for lines that start with From and a character
# followed by a two digit number between 00 and 99 followed by ':'
# Then print the number if it is greater than zero
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^From .* ([0-9]+):', line)
    if len(x) > 0:
        print(x)



k = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+',k)
print(y)


help(re.search)