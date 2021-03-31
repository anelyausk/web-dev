# https://www.hackerrank.com/challenges/capitalize/problem

def solve(s):
    for i in s.split():
        s = s.replace(i, i.capitalize())
    return s


s = input()
print(solve(s))
