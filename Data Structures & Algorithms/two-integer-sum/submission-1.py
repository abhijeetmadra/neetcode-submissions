class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        first_index = 0
        second_index = 0
  
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if i == j:
                    continue
                
                if nums[i] + nums[j] == target:
                    first_index = i
                    second_index = j
                    break

        return [first_index, second_index] if first_index < second_index else [second_index, first_index]
    
        