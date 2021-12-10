


#if 0

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int res = 0;
        if(prices.size() == 0)
            return -1;


        int minLeft;
        minLeft = prices[0];


        for(int i=1;i<prices.size();++i)
        {
            minLeft = min(minLeft,prices[i]);
            res = max(res,prices[i] - minLeft);


        }


        return res;

    }
};


int main() {
    Solution s;
    vector<int> v1{1,4,2};
    vector<int> v2{7,6,4,3,1};
        cout << s.maxProfit(v1) << endl;
        cout << s.maxProfit(v2) << endl;



    return 0;
}


#endif