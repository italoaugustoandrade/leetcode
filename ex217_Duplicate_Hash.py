''' 
217. Contains Duplicate


https://leetcode.com/problems/contains-duplicate/?envType=study-plan&id=data-structure-i
Ítalo Andrade

'''


class Solution:
    """
     Class Solution for question. 
    """

    @staticmethod
    def containsDuplicate(nums):
        """ 
            Given an integer array nums, return true if any value appears at least twice in the array, 
            and return false if every element is distinct. 

        """
        hash_dict = {}
        for num in nums:
            if num in hash_dict:
                return True
            else:
                hash_dict[num] = 1

        return False


input_fun = [1, 2, 3, 4]
output_fun = Solution.containsDuplicate(input_fun)
print(output_fun)
