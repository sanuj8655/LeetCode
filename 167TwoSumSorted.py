numbers = [-1, 0]
target = -1


def twoSum(nums, target):
    start = 0
    end = len(nums) - 1

    while start < end:
        s = nums[start] + nums[end]
        if s > target:
            end -= 1
        elif s < target:
            start += 1
        else:
            return [start + 1, end + 1]


print(twoSum(numbers, target))
