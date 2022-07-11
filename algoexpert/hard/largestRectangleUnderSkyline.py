def largestRectangleUnderSkyline(buildings):
    # Write your code here.
    stack = []
    max_area = 0
    for i, height in enumerate(buildings + [0]):
        while stack and buildings[stack[-1]] >= height:
            top = stack.pop()
            width = i if len(stack) == 0 else i - stack[-1] - 1
            cur_area = buildings[top] * width
            max_area = max(cur_area, max_area)
        stack.append(i)

    return max_area


if __name__ == '__main__':
    bs =  [3, 2]
    print(largestRectangleUnderSkyline(bs))
