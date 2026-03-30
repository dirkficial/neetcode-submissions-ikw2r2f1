class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ref = set(nums)
        res = 0
        for num in nums:
            counter = 0
            current = num
            while current in ref:
                counter += 1
                current += 1
            res = max(res, counter)
        return res