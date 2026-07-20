class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = []

        for num in nums:
            if num not in result:
                result.append(num)
            else:
                return True
        
        return False