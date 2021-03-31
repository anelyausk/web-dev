def power(a, n):
    return a ** n


a, n = [i for i in input().split()]
print(power(float(a), int(n)))
