''' 
2215. Find the Difference of Two Arrays

Ítalo Andrade

'''
from typing import List


class Solution:
    """Class Solution for question.

    Returns:
        None
    """

    @staticmethod
    def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # Find is possible, but a dict is a better solution

        hash_dict = dict()

        max_len = max(len(nums1), len(nums2))
        i = 0
        while i < max_len:
            if i < len(nums1):
                if nums1[i] in hash_dict:
                    if hash_dict[nums1[i]] == 2:
                        hash_dict[nums1[i]] = 3
                else:
                    hash_dict[nums1[i]] = 1
            if i < len(nums2):
                if nums2[i] in hash_dict:
                    if hash_dict[nums2[i]] == 1:
                        hash_dict[nums2[i]] = 3
                else:
                    hash_dict[nums2[i]] = 2
            i = i+1
        a = []
        b = []
        for key, value in hash_dict.items():
            if value == 1:
                a.append(key)
            if value == 2:
                b.append(key)

        return ([a, b])


nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
print(Solution.findDifference(nums1, nums2))
