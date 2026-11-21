class Solution:
    def isConsecutive(self, nums: list[int]) -> bool:
        n = len(nums)
        # Check 1: Ensure there are no duplicates
        if len(set(nums)) != n:
            return False
        
        # Check 2: Ensure the range matches the number of elements
        return max(nums) - min(nums) == n - 1