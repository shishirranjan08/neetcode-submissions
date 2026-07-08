class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm ={}
        for j , items in enumerate(nums):
            complement  = target - items
            if complement in hm:
                return [hm[complement],j]
            hm[items] = j

        return[]
            
        