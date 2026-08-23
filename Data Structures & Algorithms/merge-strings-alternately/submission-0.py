class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        max_len = max(len(word1), len(word2))
        res = []

        for i in range(max_len):
            if i >= len(word1):
                res.append(word2[i])
            elif i >= len(word2):
                res.append(word1[i])
            elif i < len(word1) and i < len(word2):
                res.append(word1[i] + word2[i])
        
        return "".join(res)