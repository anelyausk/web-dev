from math import sqrt
n = int(input())
i = 1

while i <= n:
    if int(sqrt(i)) == sqrt(i):
        print(i)
    i += 1
