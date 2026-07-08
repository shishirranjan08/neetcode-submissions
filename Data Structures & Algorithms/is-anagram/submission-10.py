class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm = {}
        hm1 = {}
        if len(s) != len(t):
            return False
        for items in s:
            if items not in hm:
                hm[items] =  0
            hm[items] += 1
        
        for items in t:
            if items not in hm1:
                hm1[items] = 0
            hm1[items] += 1
        if hm != hm1:
            return False
        else: 
            return True
        