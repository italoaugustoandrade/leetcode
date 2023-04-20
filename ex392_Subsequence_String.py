''' 
392. Is Subsequence
Given two strings s and t, 
return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original 
string by deleting some (can be none) of the characters without disturbing 
the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

https://leetcode.com/problems/isomorphic-strings/?envType=study-plan&id=level-1

Ítalo Andrade

'''


class Solution:
    """Class solution exercise

    Returns:
        None
    """

    @staticmethod
    def isSubsequence(s: str, t: str) -> bool:
        """
        392. Is Subsequence
        Given two strings s and t, 
        return true if s is a subsequence of t, or false otherwise.

        Args:
            s (str): string 1
            t (str): string 2

        Returns:
            bool: determine if s and t are isomorphic
        """
        j = 0
        s_len = len(s)
        t_len = len(t)

        if s_len == 0: #If s empty
            return True

        for i in range(t_len):
            if t[i] == s[j]:
                j = j+1
            if j == s_len:
                return True

        return False


input_fun1 = ""
input_fun2 = "ahbgdc"
output_fun = Solution.isSubsequence(input_fun1, input_fun2)
print(output_fun)
