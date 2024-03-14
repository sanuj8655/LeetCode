nums = [1, 2, 3, 4]


def productExceptSelf(nums):
    res = [1] * len(nums)
    for ele in range(1, len(nums)):
        res[ele] = nums[ele - 1] * res[ele - 1]
    post = 1
    for ele in range(len(nums) - 1, -1, -1):
        res[ele] = res[ele] * post
        post *= nums[ele]
    return res


print(productExceptSelf(nums))
