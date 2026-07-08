class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm ={}
        list =[]
        for items in nums:
            if items not in hm:
                hm[items] = 0
            hm[items] += 1
        
        result = sorted(hm, key=hm.get,reverse=True)
        
        return result[:k]