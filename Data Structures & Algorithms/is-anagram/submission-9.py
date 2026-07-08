class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dt = {}
        if len(s) != len(t):
            return False
        for x in s:
            dt[x] = dt.get(x,0) + 1
        for x in t:
            if x not in dt or dt[x] == 0:
                return False
            dt[x] = dt[x]-1
        return True