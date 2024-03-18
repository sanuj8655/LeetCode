from typing import List

s = "dvdf"


def lengthOfLongestSubstring(s: str) -> int:
    maxl = 0
    hashmap = {}
    l = 0
    for r in range(len(s)):
        ch = s[r]
        if ch in hashmap and hashmap[ch] >= l:
            l = hashmap[ch] + 1
        maxl = max(maxl, r - l + 1)
        hashmap[ch] = r
    return maxl


print(lengthOfLongestSubstring(s))
