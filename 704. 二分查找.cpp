//
// Created by lifan on 2021/12/10.
//
#if 0
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <unordered_set>

using namespace std;
class Solution {
public:
    int search(vector<int>& nums, int target) {

        int left = 0;
        int right = nums.size() - 1;
        while(left <= right)
        {
            int mid = left+(right - left) / 2;
            if(nums[mid] > target){
                right = mid - 1;

            }else if(nums[mid] < target){
                left = mid + 1;
            }
            else
                return mid;
        }





        return -1;
    }
};

int main()
{
    Solution s;
    vector<int> v1{1,2,3,4};
    vector<int> v2{7,7,7,7};
    vector<int> v3{-1,0,3,5,9,12};

    cout << s.search(v1,4) << endl;
    cout << s.search(v3,9) << endl;




    return 0;

}


#endif
