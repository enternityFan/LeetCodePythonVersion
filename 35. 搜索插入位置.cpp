#if 1
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <unordered_set>

using namespace std;
// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {

        int left = 0,right = nums.size() - 1;
        int mid = left + (right - left ) /2;

        while(left <=right)
        {
            if(nums[mid] <target)
            {

                left = mid + 1;

            } else if(nums[mid] > target)
            {

                right = mid - 1;
            }
            else
                return mid;
            mid = left + (right - left ) /2;

        }
        if(mid < nums.size() && nums[mid] < target)
        {
               return mid+1;


        }
        else
            return mid;

    }
};


int main()
{
    Solution s;
    vector<int> v{1,3,5,6};
    cout<< s.searchInsert(v,4)<< endl;
    cout << s.searchInsert(v,2) << endl;
    cout<<s.searchInsert(v,7) << endl;
    cout<<s.searchInsert(v,0) << endl;





    return 0;

}


#endif


//
// Created by lifan on 2021/12/13.
//

//
// Created by lifan on 2021/12/13.
//

