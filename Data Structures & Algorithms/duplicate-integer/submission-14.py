class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm = {}
        for i, items in enumerate(nums):
            if items not in hm:
                hm[items] = True
            else:
                return True
        return False

        