class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        val = set(nums)
        longest = 0
        for items in val:
           
            if items - 1 not in val:
                length = 1
                while items+length in val:
                    length +=1
                longest = max(longest,length)

        return longest
        