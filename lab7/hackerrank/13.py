# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):
    return sum(array)/len(array)


n = int(input())
a = [int(i) for i in input().split()]
print(average(set(a)))
