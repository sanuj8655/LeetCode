from typing import List

s = "()"


def isValid(s: str) -> bool:
    hash = {")": "(", "}": "{", "]": "["}
    stack = []
    for ele in s:
        if ele in hash:
            if stack and stack[-1] == hash[ele]:
                stack.pop()
            else:
                return False
        else:
            stack.append(ele)
    return True if not stack else False


print(isValid(s))
