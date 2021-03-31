# https://www.hackerrank.com/challenges/symmetric-difference/problem?h_r=next-challenge&h_v=zen

m = int(input())
a = set(map(int, input().split()))
n = int(input())
b = set(map(int, input().split()))
c = (a.difference(b)).union(b.difference(a))
for i in sorted(list(c)):
    print(i)
