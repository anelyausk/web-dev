# https://www.hackerrank.com/challenges/python-mutations/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def mutate_string(s, pos, char):
    return s[:pos] + char + s[pos+1:]


s = input()
i, c = input().split()
print(mutate_string(s, int(i), c))
