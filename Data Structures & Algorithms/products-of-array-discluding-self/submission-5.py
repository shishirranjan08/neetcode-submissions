class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len1 = len(nums)
        left =[1]*len1 
        for i in range(1,len1):
            left[i] = left[i-1] * nums[i-1]

        right = [1]*len1
        for i in range (len1-2,-1,-1):
            right[i] = right[i+1] * nums[i+1]

        result = [1]*len1

        for i in range(len1):
            result[i] = left[i]* right[i]
        
        return result