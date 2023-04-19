''' 
53. Maximum Subarray
 
https://leetcode.com/problems/maximum-subarray/?envType=study-plan&id=data-structure-i
Ítalo Andrade

'''


class Solution:
    """
     Class Solution for question. 
    """

    @staticmethod
    def maxSubArray(nums):
        """Given an integer array nums, 
        find the subarray with the largest sum, 
        and return its sum.

        Args:
            nums (int): nums to find the subarray with the largest sum

        Returns:
            int: sum
        """


        len_nums = len(nums)
        i = 0
        sum_ant = 0
        best_sum = -10**4

        while i <= len_nums-1:
            if nums[i] > sum_ant + nums[i]:
                sum_ant = nums[i]
            else:
                sum_ant = sum_ant+nums[i]
            if sum_ant > best_sum:
                best_sum = sum_ant
            i = i+1
        return best_sum




input_fun = [1,2]
output_fun = Solution.maxSubArray(input_fun)
print(output_fun)
