class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
            count = {}
            left  = 0
            longest =0

            for right in range(len(s)):
                count[s[right]] = count.get(s[right],0)+1
                
                window_size = right-left +1
                most_common = max(count.values())
                changes_needed = window_size - most_common

                if (changes_needed > k):
                    count[s[left]] -= 1
                    left += 1
                
                longest = max(longest, right-left+1)
            
            return longest