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
    int numberOfArithmeticSlices(vector<int>& nums) {


        /*
         *
         *
         * 1.判断当前是不是等查数列，如果不是，指针直接向后面移动+2
         * 2.如果是等查数列，就+j++，一直是，一直加，直到不是，就把设j为1
         *
         *
         */
        if(nums.size() <= 2)
            return 0;
        vector<int> a{0,0};
        int res=0;
        int d=0;
        int last_d = 0;
        int j = 1;
        for(int i=2;i<nums.size();++i) {

            if(nums[i] - nums[i-1] == nums[i-1] - nums[i-2])
            {
                res +=j++;


            }
            else
            {
                j = 1;
                ++i;
            }


            /*
             * 下面代码可以优化。。
            if (nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]) {
                d = nums[i] - nums[i - 1];
                if (i>2)
                    last_d = nums[i-2] - nums[i-3];
                else
                    last_d = d;


                if(last_d == d)
                    res +=j++;
                else
                    res += 1;

            } else
            {
                j = 1;
            }*/
        }


        return res;


    }
};


int main()
{
    Solution s;
    vector<int> v1{1,2,3,4,5,6};
    vector<int> v2{7,7,7,7};
    vector<int> v3{3,-1,-5,-9};

    cout << s.numberOfArithmeticSlices(v1) << endl;
    cout << s.numberOfArithmeticSlices(v2) << endl;
    cout << s.numberOfArithmeticSlices(v3) << endl;





    return 0;

}


#endif
//
// Created by lifan on 2021/12/11.
//

