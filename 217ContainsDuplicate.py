def containsDuplicate(nums) -> bool:
    di = dict()
    for ele in nums:
        if ele not in di.keys():
            di[ele] = 1
        else:
            return True
    return False


nums = [1, 2, 3, 1]
print(containsDuplicate(nums))
