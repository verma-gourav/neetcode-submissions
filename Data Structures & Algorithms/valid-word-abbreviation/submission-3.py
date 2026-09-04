class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if word == abbr:
            return True
        
        p1 = p2 = 0

        while p1 < len(word) and p2 < len(abbr):
            if abbr[p2] == "0":
                return False
            
            if word[p1] == abbr[p2]:
                p1 += 1
                p2 += 1
            elif abbr[p2].isdigit():
                sub_len = 0
                while p2 < len(abbr) and abbr[p2].isdigit():
                    sub_len = sub_len * 10 + int(abbr[p2])
                    p2 += 1
                p1 += sub_len
            else:
                return False
        
        return p1 == len(word) and p2 == len(abbr)

        

