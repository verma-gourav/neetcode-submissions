class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        window_max = []
        for r in range(k - 1, len(nums)):
            window = nums[l:r+1]
            window_max.append(max(window))
            l += 1
        return window_max