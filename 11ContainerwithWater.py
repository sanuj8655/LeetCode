height = [1, 8, 6, 2, 5, 4, 8, 3, 7]


def maxArea(height):
    start = 0
    end = len(height) - 1
    hold = 0

    while start < end:
        h = min(height[start], height[end])
        w = end - start
        v = h * w
        if hold < v:
            hold = v
        if height[start] < height[end]:
            start += 1
        else:
            end -= 1
    return hold


print(maxArea(height))
