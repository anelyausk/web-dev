x = input()
answ = 0

for i in range(len(x)):
    answ += int(x[i]) * pow(2, len(x)-1-i)

print(answ)
