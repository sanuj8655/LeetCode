from collections import defaultdict

nums = [1, 1, 1, 2, 2, 3]
k = 2


def topKFrequent(nums, k):
    count = {}
    freq = [[] for ele in range(len(nums) + 1)]

    for ele in nums:
        count[ele] = 1 + count.get(ele, 0)

    for key, val in count.items():
        freq[val].append(key)

    res = []
    for ele in range(len(freq) - 1, 0, -1):
        for ele2 in freq[ele]:
            res.append(ele2)
            if len(res) == k:
                return res


print(topKFrequent(nums, k))
