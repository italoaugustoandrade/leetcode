''' 
283. Move Zeroes

Ítalo Andrade

'''


from typing import List


class Solution:
    """Class Solution for question.

    Returns:
        None
    """

    @staticmethod
    def moveZeroes(nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j=0
        while j < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
            else:
                i = i+1
            j=j+1


a = [0, 1, 0, 3, 12]

Solution.moveZeroes(a)
