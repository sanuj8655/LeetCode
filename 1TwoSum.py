nums = [3, 2, 4]
target = 6


def twoSum(nums, target):
    hashmap = {}
    for i, val in enumerate(nums):
        rem = target - nums[i]
        if rem in hashmap:
            return [hashmap[rem], i]
        hashmap[val] = i


print(twoSum(nums, target))
