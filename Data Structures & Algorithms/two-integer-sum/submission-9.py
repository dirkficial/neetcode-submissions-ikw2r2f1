class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in res.keys():
                return [res[complement], i]
            res[n] = i
        