#include<iostream>
#include<string>
#include <vector>
#include<cmath>
#include <numeric> 

using namespace std;

class Solution {

    /*
    Class Solution for question.

    Returns:
        None
    """
    */

public:
    double findMaxAverage(vector<int>& nums, int k) {
        int j=0;
        double max_avg=-pow(10,4);
        double soma,avg;
        soma=accumulate(nums.begin(),nums.begin()+k,0);
        while (true){
            avg=soma/k;
            if (avg>max_avg){
                max_avg=avg;
            }
            if (j>= (nums.size()-k)){
                break;
            }
            soma=soma-nums[j]+nums[j+k];
            j=j+1;
        } 
        return max_avg;

    }
};

int main()
{
   
    Solution solve;

    vector<int> numbers = {1,12,-5,-6,50,3};
    int k = 4;

    cout<<solve.findMaxAverage(numbers,k);


    return 0;
}