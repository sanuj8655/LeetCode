nums = [100, 4, 200, 1, 3, 2]


def longestConsecutive(nums):
    s = set(nums)
    longest = 0
    for ele in nums:
        if (ele - 1) not in s:
            length = 0
            while (ele + length) in s:
                length += 1
            longest = max(longest, length)
    return longest


print(longestConsecutive(nums))
