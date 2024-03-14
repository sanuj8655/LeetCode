nums = [-1, 0, 1, 2, -1, -4]


# [-4, -1, -1, 0, 1, 2]
def threeSum(nums):
    nums.sort()
    ans = []
    for ele in range(len(nums) - 2):
        if ele > 0 and nums[ele] == nums[ele - 1]:
            continue
        l = ele + 1
        r = len(nums) - 1
        while l < r:
            total = nums[ele] + nums[l] + nums[r]
            if total > 0:
                r -= 1
            elif total < 0:
                l += 1
            else:
                triplet = [nums[ele], nums[l], nums[r]]
                ans.append(triplet)
                while l < r and nums[l] == triplet[1]:
                    l += 1
                while l < r and nums[r] == triplet[2]:
                    r -= 1
    return ans


print(threeSum(nums))
