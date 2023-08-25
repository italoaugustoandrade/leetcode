''' 
1456. Maximum Number of Vowels in a Substring of Given Length

Ítalo Andrade

'''
from typing import List
class Solution:
    """Class Solution for question.

    Returns:
        None
    """

    @staticmethod
    def maxVowels(s: str, k: int) -> int:
        i = 0
        count=0
        max_count =-1
        while i<len(s):
            if s[i] in ['a','e','i','o','u']:
                count=count+1
            if i>=k:
               if s[i-k] in ['a','e','i','o','u']:
                count=count-1
            if count>max_count:
                max_count=count

            i=i+1
        return max_count




a = "leetcode"
b= 3
print(Solution.maxVowels(a,b))
        