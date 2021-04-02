def front_times(str, n):
    res = ''
    for i in range(n):
        if len(str) <= 3:
            res += str
        else:
            res += str[:3]
    return res


front_times('Chocolate', 2)
