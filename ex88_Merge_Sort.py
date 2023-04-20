''' 
88. Merge Sorted Array
 
https://leetcode.com/problems/merge-sorted-array/?envType=study-plan&id=data-structure-i
Ítalo Andrade

'''


from typing import List


class Solution:
    """
     Class Solution for question. 
    """

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
        and two integers m and n, representing the number of elements in nums1 and nums2 
        respectively.
        The final sorted array should not be returned by the function, but instead be stored 
        inside the array nums1. To accommodate this, nums1 has a length of m + n, where the 
        first m elements denote the elements that should be merged, and the last n elements 
        are set to 0 and should be ignored. nums2 has a length of n.

        Returns:
            None
        """
        MAX_LEN = 200
        i = 0
        j = 0
        if m == 0:
            nums1[:] = nums2[:]
            i = MAX_LEN
        if n == 0:
            i = MAX_LEN

        while i < len(nums1):
            #Compare order. Insert in the position and remove the last  
            if nums1[i] > nums2[j]: 
                nums1.insert(i, nums2[j])
                nums1.pop()
                j = j+1

            if nums1[i] == 0 and i >= m+j:
                nums1[i] = nums2[j]
                j = j+1
            if j >= n:
                break
            i = i+1



f1 = [-1, 3, 0, 0, 0, 0, 0]
len1 = 2
f2 = [0, 0, 1, 2, 3]
len2 = 5
output_fun = Solution()
output_fun.merge(f1, len1, f2, len2)
print(output_fun)
