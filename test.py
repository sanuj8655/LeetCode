from typing import List
s = "tmmzuxt"
def lengthOfLongestSubstring(s: str) -> int:
    maxl = 0
    for ele in range(len(s)):
        string = ""
        length = 0
        for ele2 in range(ele, len(s)):
            if s[ele2] not in string:
                string += s[ele2]
                length += 1
            else:
                break
        maxl = max(maxl, length)
    return maxl


print(lengthOfLongestSubstring(s))