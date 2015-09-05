#https://www.hackerrank.com/challenges/string-validators
s = input()
results = [False]*5
i = 0
while i<len(s):
    if results != [True]*5:
        if s[i].isalpha():
            results[0]=True
            results[1]=True
            if s[i].isupper():
                results[4]=True
            elif s[i].islower():
                results[3]=True
        if s[i].isdigit():
            results[0]=True
            results[2]=True
        i += 1
    else:
        break
for x in results:
    print(str(x))
