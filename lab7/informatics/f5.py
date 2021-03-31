n = int(input())
cnt = 0
a = [int(i) for i in input().split()]

for i in range(1, n - 1):
    if a[i] > a[i + 1] and a[i - 1] < a[i]:
        cnt += 1

print(cnt)
