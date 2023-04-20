''' 
1. Two Sum

Ítalo Andrade

'''


from typing import List


class Solution:
    """Class Solution for question.

    Returns:
        None
    """

    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers nums and an integer target, 
        return indices of the two numbers such that they add up to target.

        You may assume that each input would have exactly one solution, 
        and you may not use the same element twice.

        You can return the answer in any order.

        Args:
            nums (List[int]): array of integers nums
            target (int): integer target for reach

        Returns:
            List[int]: indices of the two numbers
        """
        key_dict = {}
        for i, num in enumerate(nums):
            complement = target-num
            if complement in key_dict:
                return [key_dict[complement], i]

            key_dict[nums[i]] = i


input_fun1 = [3, 2, 4]
input_fun2 = 6
output_fun = Solution.twoSum(input_fun1, input_fun2)
print(output_fun)
