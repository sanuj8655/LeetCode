def isAnagram(s: str, t: str):
    di = dict()
    for ele in s:
        if ele in di.keys():
            di[ele] += 1
        else:
            di[ele] = 1

    for ele in t:
        if ele in di.keys():
            di[ele] -= 1
        else:
            di[ele] = 1

    for ele in di.values():
        if ele != 0:
            return False
    return True


s = "rat"
t = "car"
print(isAnagram(s, t))
