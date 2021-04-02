def big_diff(nums):
    minimum = nums[0]
    maximum = nums[0]

    for i in nums:
        minimum = min(minimum, i)
        maximum = max(maximum, i)

    return maximum - minimum
