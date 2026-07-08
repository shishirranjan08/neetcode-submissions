class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(ch.lower() for ch in s if ch.isalnum())
        len1 = len(s)
        start = 0
        end = len1-1
        while(start < end):
            if(s[start] != s[end]):
                return False
            start += 1
            end -= 1
        return True
                
