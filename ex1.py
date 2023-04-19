''' 
1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

https://leetcode.com/problems/isomorphic-strings/?envType=study-plan&id=level-1

Ítalo Andrade

'''


from typing import List


class Solution:
    """Class solution exercise

    Returns:
        None
    """

    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        """_summary_

        Args:
            nums (List[int]): _description_
            target (int): _description_

        Returns:
            List[int]: _description_
        """
        Hash = {}
        for i, num in enumerate(nums):
            id = target-num
            if id in Hash:
                return [Hash[id], i]
            else:
                Hash[nums[i]] = i


input_fun1 = [3, 2, 4]
input_fun2 = 6
output_fun = Solution.twoSum(input_fun1, input_fun2)
print(output_fun)
