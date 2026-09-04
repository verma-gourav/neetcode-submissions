class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if word == abbr:
            return True
        
        m, n = len(word), len(abbr)
        p1 = p2 = 0

        while p1 < m and p2 < n:
            if abbr[p2] == "0":
                return False
            
            if word[p1] == abbr[p2]:
                p1 += 1
                p2 += 1
            elif abbr[p2].isdigit():
                num = 0
                while p2 < n and abbr[p2].isdigit():
                    num = num * 10 + int(abbr[p2])
                    p2 += 1
                p1 += num
            else:
                return False
        
        return p1 == m and p2 == n
 
        

