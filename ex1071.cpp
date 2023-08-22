#include<iostream>
#include<string>
using namespace std;

class Solution {

    /*
    Class Solution for question.

    Returns:
        None
    """
    */

public:
    string gcdOfStrings(string str1, string str2) {
        
        std::cout<<"Printei";

        int div, i=0, j=0;
        div=str2.length();
        while(true){

            if (div==0)
                return ("");
            
            if ((str1.length()%div==0)&&(str2.length()%div==0)){

                while (i<str1.length()){ 
                    if (str1.substr(i,div) == str2.substr(j,div)){
                        i=i+div;
                        if (j<str2.length()-div)
                            j=j+div;
                    } else {
                        return ("");
                    }
                    if (i == str1.length())
                       return (str2.substr(0,div));
                }
                j=0;
                i=0;
                div=div-1;
            }
            else{
                div=div-1;
            }
            
        }
    }
};

int main()
{
   
    Solution solve;

    string str1,str2;
    str1="ABABABABAB";
    str2="ABAB";

    std::cout<<solve.gcdOfStrings(str1,str2);

    return 0;
}

// class Solution:
//     def gcdOfStrings(self, str1: str, str2: str) -> str:
//         div=len(str2)
//         i=0
//         j=0
//         while True:
//             if div==0:
//                 return ""
//             if len(str1)%div==0 and len(str2)%div==0:
//                 while i<len(str1):
//                     if str1[i:i+div] == str2[j:div+j]:
//                         i=i+div
//                         if j<len(str2)-div:
//                             j=j+div
//                     else:
//                         #  div=int(div/2);   
//                         # break 
//                         return "" 
//                     if i==len(str1):
//                         return str2[0:div]
//                 i=0
//                 j=0
//                 div=div-1;
//             else:
//                 div=div-1;