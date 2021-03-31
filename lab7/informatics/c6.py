def xor(x, y):
    if x == 1 and y == 1:
        return 0
    elif x == 1 or y == 1:
        return 1
    else:
        return 0


x, y = [int(i) for i in input().split()]
print(xor(x, y))