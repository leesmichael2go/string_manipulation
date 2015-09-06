#https://www.hackerrank.com/challenges/pangrams
s = input().lower().replace(' ','')
asciiList = []
for i in range(0,len(s)):
    asciiList.append(ord(s[i]))
for i in range(ord('a'), ord('z')+1):
    if i in asciiList:
        i += 1
    else:
        print("not pangram")
        break
    if i == ord('z'):
        print("pangram")
