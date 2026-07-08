class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        need = Counter(t)
        missing = len(t)

        left = 0
        best_start=0
        best_len=float("inf")

        for right in range(len(s)):
            letter = s[right]
            
            if need[letter] >0:
                missing -= 1
            need[letter] -= 1

            while missing == 0:
                if right-left+1 <best_len:
                    best_start = left
                    best_len = right-left +1

                need[s[left]] +=1
                if need[s[left]] > 0:
                    missing += 1
                left += 1

        return "" if best_len == float("inf") else s[best_start:best_start + best_len]