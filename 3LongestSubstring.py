from typing import List

s = "tmmzuxt"


# Time - O(n3)
# def lengthOfLongestSubstring(s: str) -> int:
#     maxl = 0
#     for ele in range(len(s)):
#         string = ""
#         length = 0
#         for ele2 in range(ele, len(s)):
#             if s[ele2] not in string:
#                 string += s[ele2]
#                 length += 1
#             else:
#                 break
#         maxl = max(maxl, length)
#     return maxl

# Time - O(n)
def lengthOfLongestSubstring(s: str) -> int:
    seen = {}
    length = 0
    l = 0
    for r in range(len(s)):
        ch = s[r]
        if ch in seen and seen[ch] >= l:
            l = seen[ch] + 1
        else:
            length = max(length, r - l + 1)
        seen[ch] = r

    return length


print(lengthOfLongestSubstring(s))
