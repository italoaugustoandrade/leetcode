''' 
1480. Running Sum of 1d Array

https://leetcode.com/problems/running-sum-of-1d-array/
Ítalo Andrade

'''


class Solution:
    """
    Class Solution for question. 

    Returns:
        None
    """

    @staticmethod
    def runningSum(nums):
        """
        Given an array nums. We define a running sum of an array as 
        runningSum[i] = sum(nums[0]…nums[i]).
        Return the running sum of nums.
        Args:
            nums (int): list of numbers to sum.
        Returns:
            sum_out (int): list of sum
        """
        sum_nums = 0
        sum_out = []
        for num in nums:
            sum_nums = sum_nums+num
            sum_out.append(sum_nums)

        return sum_out


input_fun = [3, 1, 2, 10, 1]
output_fun = Solution.runningSum(input_fun)
print(output_fun)
