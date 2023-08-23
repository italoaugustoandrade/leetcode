#include<iostream>
#include<string>
#include <vector>

using namespace std;

class Solution {

    /*
    Class Solution for question.

    Returns:
        None
    """
    */

public:
    void moveZeroes(vector<int>& nums) {
        int i=0;
        for (int j=0; j<nums.size();++j){
            if (nums[i]==0){
                nums.push_back(0);
                nums.erase(nums.begin()+i);
            } else{
                ++i;

            }
        }
    }

    void moveZeroes1(vector<int>& nums) {
        int id_zero=0,id_postivo=0;
        for (int j=0; j<nums.size();++j){
            if (nums[j]!=0){
                nums[id_postivo]=nums[j];
                ++id_postivo;

            } else{
                ++id_zero;
            }
        }
        for (int j=nums.size()-1;j>nums.size()-id_zero-1;--j){
            nums[j]=0;
        }
    }
    
};

int main()
{
   
    Solution solve;

    vector<int> numbers = {0, 1, 0};

    solve.moveZeroes1(numbers);


    return 0;
}