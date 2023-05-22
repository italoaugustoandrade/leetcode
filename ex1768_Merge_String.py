''' 
1768. Merge Strings Alternately

Ítalo Andrade

'''


from typing import List


class Solution:
    """Class Solution for question.

    Returns:
        None
    """

    @staticmethod
    def mergeAlternately1(word1: str, word2: str) -> str:
        """
    You are given two strings word1 and word2. 
    Merge the strings by adding letters in alternating order, 
    starting with word1. If a string is longer than the other, 
    append the additional letters onto the end of the merged string.

    Return the merged string.

        Args:
            word1(str): word merge 1
            word2 (str): word merge 2

        Returns:
            word3(str): merge entre word 1 e word2 
        """
        len_word1=len(word1)
        len_word2=len(word2)
        word3=""
        for i in range(max(len_word1,len_word1)):
            word3=word3+word1[i]+word2[i]
            if i==len_word1-1:
                word3=word3+word2[i+1:len_word2]
                return word3
            if i==len_word2-1:
                word3=word3+word1[i+1:len_word1]
                return word3
        return word3

    @staticmethod
    def mergeAlternately(word1: str, word2: str) -> str:
        """
    You are given two strings word1 and word2. 
    Merge the strings by adding letters in alternating order, 
    starting with word1. If a string is longer than the other, 
    append the additional letters onto the end of the merged string.

    Return the merged string.

        Args:
            word1(str): word merge 1
            word2 (str): word merge 2

        Returns:
            word3(str): merge entre word 1 e word2 
        """
        word3=[]
        for i in range(min(len(word1),len(word2))):
            word3.append(word1[i]+word2[i])
        return ''.join(word3) + word1[i+1:] + word2[i+1:]



input_fun1 = "abcd"
input_fun2 = "PQ"
output_fun = Solution.mergeAlternately(input_fun1, input_fun2)
print(output_fun)
