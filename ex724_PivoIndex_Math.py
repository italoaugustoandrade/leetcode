''' 
724. Find Pivot Index


https://leetcode.com/problems/find-pivot-index/?envType=study-plan&id=level-1
Ítalo Andrade

'''


from typing import List


class Solution:
    """    
    Class Solution for question. 
    
    Returns:
        None
    """

    @staticmethod
    def pivotIndex(nums: List[int]) -> int:
        """
        Given an array of integers nums, calculate the pivot index of this array.

        The pivot index is the index where the sum of all the numbers strictly to the left of the 
        index is equal to the sum of all the numbers strictly to the index's right.

        If the index is on the left edge of the array, then the left sum is 0 
        because there are no elements to the left. This also applies to the right edge of the array.

        Return the leftmost pivot index. If no such index exists, return -1.

        Args:
            nums (List[int]): nums for sum

        Returns:
            int: return index that split the sum 
        """

        sum_ant=0
        sum_actual=0
        sum_all=sum(nums)
        i=0
        for num in nums:
            sum_ant=sum_actual
            if sum_ant==(sum_all-sum_ant-num):
                return i
            sum_actual = sum_actual+num
            i=i+1
        return -1


input_fun=[-1,-1,-1,-1,-1,0]
output_fun=Solution.pivotIndex(input_fun)
print(output_fun)
