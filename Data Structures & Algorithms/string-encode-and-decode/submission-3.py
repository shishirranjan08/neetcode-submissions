class Solution:

    def encode(self, strs: List[str]) -> str:
        result =""
        for words in strs:
            result  += str(len(words)) + "#" + words

        return result

    def decode(self, s: str) -> List[str]:
        result =[]
        i=0
        
        while(i<len(s)):
            hash_pos = s.find('#',i)
            length = int(s[i:hash_pos])
            word_start = hash_pos + 1
            word = s[word_start:word_start + length]
            result.append(word)
            i = word_start + length
        return result
        



