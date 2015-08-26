#https://www.hackerrank.com/contests/pythonist2/challenges/swap-case
import string
s = list(input())
new = []
for c in s:
    if c in list(string.ascii_letters):
        new.append(c.swapcase())
    else:
        new.append(c)
print(''.join(new))