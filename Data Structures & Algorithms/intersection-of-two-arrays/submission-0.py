class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set(nums1)
        result = set()
        for number in nums2:
            if number in nums1_set:
                result.add(number)
        return list(result)
