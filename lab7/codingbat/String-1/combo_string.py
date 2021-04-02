def combo_string(a, b):
    if min(len(a), len(b)) == len(a):
        return a + b + a
    return b + a + b


print(combo_string('Hello', 'Hiiiiiiiii'))
