class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        if len(nums) > 0:
            for number in nums:
                if number not in count:
                    count[number] = 1
                else:
                    count[number] += 1
                    
        temp = sorted(count.items(),key=lambda x: x[1],reverse=True)[:k]
        result = [key for key,value in temp]

        return result
        