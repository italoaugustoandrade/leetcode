''' 
643. Maximum Average Subarray I

Ítalo Andrade

'''
from typing import List
class Solution:
    """Class Solution for question.

    Returns:
        None
    """

    @staticmethod
    def findMaxAverage(nums: List[int], k: int) -> float:
        j=0
        max_avg=-pow(10,4)
        while j<=(len(nums)-k):
            avg=sum(nums[j:j+k])/k
            j=j+1
            if avg>max_avg:
                max_avg=avg
        return max_avg
    
    @staticmethod
    def findMaxAverage1(nums: List[int], k: int) -> float:
        j=0
        max_avg=-pow(10,4)
        soma=sum(nums[j:j+k])
        while True:
            avg=soma/k
            if avg>max_avg:
                max_avg=avg
            if j>=(len(nums)-k):
                break
            soma=soma-nums[j]+nums[j+k]
            j=j+1
        return max_avg

a = [0,1,1,3,3]
b= 4
print(Solution.findMaxAverage1(a,b))
        