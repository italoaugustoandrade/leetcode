''' 
1071. Greatest Common Divisor of Strings

Ítalo Andrade

'''


from typing import List


class Solution:
    """Class Solution for question.

    Returns:
        None
    """

    @staticmethod
    def gcdOfStrings(str1: str, str2: str) -> str:
        """
    For two strings s and t, we say "t divides s" if and only 
    if s = t + ... + t (i.e., t is concatenated with itself one 
    or more times). Given two strings str1 and str2, 
    return the largest string x such that x 
    divides both str1 and str2.

        """

        div = len(str2)
        i = 0
        j = 0
        while True:
            if div == 0:
                return ""
            if len(str1) % div == 0 and len(str2) % div == 0:
                while i < len(str1):
                    if str1[i:i+div] == str2[j:div+j]:
                        i = i+div
                        if j < len(str2)-div:
                            j = j+div
                    else:
                        return ""
                    if i == len(str1):
                        return str2[0:div]
                i = 0
                j = 0
                div = div-1
            else:
                div = div-1


input_fun1 = "AAAAAAAAA"
input_fun2 = "AAACCC"
output_fun = Solution.gcdOfStrings(input_fun1, input_fun2)
print(output_fun)
