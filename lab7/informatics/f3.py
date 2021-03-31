x = int(input())
answ = 0

while x > 0:
    answ = answ*10 + x % 10
    x = x // 10

print(answ)
