''' 
205. Isomorphic Strings
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced 
to get t.

All occurrences of a character must be replaced with another character while
preserving the order of characters. No two characters may map to the same 
character, but a character may map to itself.

https://leetcode.com/problems/isomorphic-strings/?envType=study-plan&id=level-1

Ítalo Andrade

'''


class Solution:
    """Class solution exercise

    Returns:
        None
    """

    @staticmethod
    def isIsomorphic(s: str, t: str) -> bool:
        """
        205. Isomorphic Strings
        Given two strings s and t, determine if they are isomorphic.

        Two strings s and t are isomorphic if the characters in s can be replaced 
        to get t.

        All occurrences of a character must be replaced with another character while
        preserving the order of characters. No two characters may map to the same 
        character, but a character may map to itself.

        Args:
            s (str): string 1
            t (str): string 2

        Returns:
            bool: determine if s and t are isomorphic
        """
        str_len = len(s)
        hash_s = {}
        hash_t = {}
        for i in range(str_len):
            if s[i] in hash_s and t[i] in hash_t:
                if hash_s[s[i]] != hash_t[t[i]]:
                    return False
            else:
                if s[i] in hash_s or t[i] in hash_t:
                    return False
                else:
                    hash_s[s[i]] = i
                    hash_t[t[i]] = i
        return True


input_fun1 = "paper"
input_fun2 = "title"
output_fun = Solution.isIsomorphic(input_fun1, input_fun2)
print(output_fun)
