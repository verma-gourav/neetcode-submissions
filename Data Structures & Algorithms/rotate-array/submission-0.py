class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        queue = deque(nums)

        for i in range(k):
            val = queue.pop()
            queue.appendleft(val)
        
        nums[:] = list(queue)