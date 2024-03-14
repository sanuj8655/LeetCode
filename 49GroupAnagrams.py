from collections import defaultdict


def groupAnagrams(strs):
    hashmap = defaultdict(list)
    for ele in strs:
        arr = [0] * 26
        for ele2 in ele:
            arr[ord(ele2) - ord("a")] += 1
        print(arr, ele)
        hashmap[tuple(arr)].append(ele)
    return hashmap.values()


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
