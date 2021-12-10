


#if 0

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int res = 0;
        if(prices.size() < 2)
            return res;

        int minLeft=prices[0];

        int tempRes = 0;
        for(int i=1;i<prices.size();++i)
        {
            if(prices[i] - minLeft < tempRes)
            {
                // 数组不是一直增
                res +=tempRes;
                minLeft = prices[i];
                tempRes = 0;
            }
            else
            {
                //数组锁不减的
                tempRes = prices[i] - minLeft;

            }

        }
        res +=tempRes;
        res = max(res,tempRes);

        return res;
    }
};


int main() {
    Solution s;
    vector<int> v1{7,1,5,3,6,4};
    vector<int> v2{7,6,4,3,1};
    vector<int> v3{6,1,3,2,4,7};
        cout << s.maxProfit(v1) << endl;
        cout << s.maxProfit(v2) << endl;
        cout << s.maxProfit(v3) << endl;


    return 0;
}


#endif

