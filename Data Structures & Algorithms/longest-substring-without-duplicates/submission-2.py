class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l= 0
        max_window = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            max_window = max(max_window, r - l + 1)
        return max_window