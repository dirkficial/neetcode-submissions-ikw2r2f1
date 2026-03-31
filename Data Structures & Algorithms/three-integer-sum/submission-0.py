class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for idx, curr in enumerate(nums):
            if curr > 0:
                break

            if idx > 0 and curr == nums[idx - 1]:
                continue
            i, j = idx + 1, len(nums) - 1
            while i < j:
                threeSum = curr + nums[i] + nums[j]
                if threeSum > 0:
                    j -= 1
                elif threeSum < 0:
                    i += 1
                else:
                    res.append([curr, nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while nums[i] == nums[i - 1] and i < j:
                        i += 1
        return res