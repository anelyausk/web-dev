def caught_speeding(speed, is_birthday):
  if not is_birthday:
    if speed <= 60:
      return 0
    elif 61 <= speed <= 80:
      return 1
    elif speed >= 81:
      return 2
  return caught_speeding(speed-5, False)



print(caught_speeding(65, True))
