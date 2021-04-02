def array123(nums):
    seq = [1, 2, 3]
    for i in range(len(nums)):
        sub = nums[i:i + 3]
        if sub == seq:
            return True
    return False


print(array123([1, 1, 2, 4, 1]))
