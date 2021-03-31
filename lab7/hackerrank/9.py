# https://www.hackerrank.com/challenges/text-wrap/problem
import textwrap


def wrap(line, max_width):
    return textwrap.fill(string, max_width)


string = input()
max_width = int(input())
wrap(string, max_width)
