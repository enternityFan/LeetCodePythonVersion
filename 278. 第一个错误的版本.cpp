#if 0
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
    int bad = 1;
    int firstBadVersion(int n) {
        int left=0,right = n;
        int mid = left +(right - left) / 2;
        int last_mid = mid;
        bool last_res = true,res = last_res;
        while(left !=right)
        {
            res = isBadVersion(mid);
            if(res == true) // 结果在mid的左边或者就是mid
            {
                if(isBadVersion(mid-1) != true)
                    return mid;
                right = mid-1;

            }
            else{
                if(isBadVersion(mid+1) != false)
                    return mid+1;
                left = mid+1;
            }

               mid = left +(right - left) / 2;
        }


    }
    bool isBadVersion(const int value){
        if(value >= bad)
            return true;
        else
            return false;
    }
};



int main()
{
    Solution s;
    vector<vector<int>> v;
    cout <<s.firstBadVersion(1) << endl;




    return 0;

}


#endif


//
// Created by lifan on 2021/12/13.
//

