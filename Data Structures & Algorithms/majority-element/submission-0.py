class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in range(len(nums)):
            if candidate is None:
                candidate = nums[num]
                count = 1

            elif candidate != nums[num] and count == 0:
                candidate = nums[num]
                count = 1

            elif candidate != nums[num] and count != 0:
                count -= 1

            elif candidate == nums[num]:
                count += 1

        return candidate 