# arrays

n = int(input())
a = []
cnt = 0

a = input().split()

for i in range(n):
    a[i] = int(a[i])
    if a[i] > 0:
        cnt += 1

print(cnt)
