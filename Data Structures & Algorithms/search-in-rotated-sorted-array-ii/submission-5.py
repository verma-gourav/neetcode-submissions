class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                return True
            
            # for duplicated -> if boundaries and mid are identical -> shrink
            if nums[l] == nums[m] == nums[r]:
                l += 1
                r -= 1
                continue
            
            # left side sorted
            elif nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            
            # right side sorted
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        
        return False