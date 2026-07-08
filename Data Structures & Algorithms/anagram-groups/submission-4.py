class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ghm = defaultdict(list)
        for words in strs:
            count = [0]*26
            for ch in words:
                count[ord(ch) - ord("a")] += 1
            ghm[tuple(count)].append(words)
        return list(ghm.values())
                