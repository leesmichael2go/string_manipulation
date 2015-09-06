#https://www.hackerrank.com/challenges/funny-string

T = int(input())
for i in range(0,T):
    S = input()
    R = S[::-1]
    N = len(S)
    n = 1
    while n < N:
        if abs(ord(S[n])-ord(S[n-1])) == abs(ord(R[n])-ord(R[n-1])):
            n += 1
        else:
            print("Not Funny")
            break
        if n == N-1:
            print("Funny")
