class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Intution: Brute Force
        # set pointer i and j where j is bigger than i by 1
        # Check every single pair 
        # If nothing, increment i by one and restart
        i = 0
        j = i + 1
        while i < len(numbers) - 1:
            if j == len(numbers):
                i += 1
                j = i + 1
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            else:
                j += 1
