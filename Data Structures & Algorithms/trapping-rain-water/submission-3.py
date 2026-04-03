class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        l, r = 0, length
        leftMax, rightMax = height[0], height[length - 1]

        area = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                area += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                area += rightMax - height[r]

        return area