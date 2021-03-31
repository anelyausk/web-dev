# arrays

n = int(input())
a = []
cnt = 0

a = input().split()

for i in range(n):
    a[i] = int(a[i])
for i in range(n-1):
    if a[i] < a[i + 1]:
        cnt += 1

print(cnt)
