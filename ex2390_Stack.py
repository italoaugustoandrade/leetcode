''' 
2390. Removing Stars From a String

Ítalo Andrade

'''
from typing import List


class Solution:
    """Class Solution for question.

    Returns:
        None
    """

    @staticmethod
    def removeStars(s: str) -> str:
        t=[]
        for letra in s:
            if letra=='*':
                if t:
                    t.pop()
            else:
                t.append(letra)

        return "".join(t)
    

str0='*leet**cod*e'
nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
print(Solution.removeStars(str0))
