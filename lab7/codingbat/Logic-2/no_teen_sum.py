def no_teen_sum(a, b, c):
  return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(x):
  if 13 <= x <= 19 and x != 15 and x != 16:
    return 0
  return x
