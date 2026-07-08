class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm = {}
        for x in nums:
            if x in hm:
                return True
            else:
                hm[x] = 1
        return False