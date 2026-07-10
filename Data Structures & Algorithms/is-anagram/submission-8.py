class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)

        return sorted(s_list) == sorted(t_list)