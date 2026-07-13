class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = sorted(nums1 + nums2)
        if len(arr) % 2 != 0:
            return arr[int(len(arr) / 2)]
        else:
            return (arr[int(len(arr) / 2)] + arr[int((len(arr) - 1) / 2)]) / 2