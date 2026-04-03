class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        leftMax = [0] * length
        rightMax = [0] * length

        area = 0

        leftMax[0]= height[0]
        rightMax[length - 1] = height[length - 1]

        for i in range(1, length - 1):
            leftMax[i] = max(height[i], leftMax[i - 1])
        for i in range(length - 2, 0, -1):
            rightMax[i] = max(height[i], rightMax[i + 1])

        for i in range(0, length - 1):
            if height[i] > min(leftMax[i], rightMax[i]):
                continue
            area += min(leftMax[i], rightMax[i]) - height[i]

        return area