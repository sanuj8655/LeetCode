s = "A man, a plan, a canal: Panama"


def isPalindrome(s):
    start = 0
    end = len(s) - 1
    while start < end:
        if not s[start].isalnum():
            start += 1
        elif not s[end].isalnum():
            end -= 1
        elif start > end or s[start].lower() != s[end].lower():
            return False
        else:
            start += 1
            end -= 1
    return True


print(isPalindrome(s))
