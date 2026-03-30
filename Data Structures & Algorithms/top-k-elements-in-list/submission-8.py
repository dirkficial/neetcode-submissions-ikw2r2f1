class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        ans = []

        for n in nums:
            count[n] = count.get(n, 0) + 1
        for i, c in count.items():
            freq[c].append(i)
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                ans.append(j)
                if len(ans) == k:
                    return ans