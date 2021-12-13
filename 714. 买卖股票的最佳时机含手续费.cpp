//
// Created by lifan on 2021/12/10.
//




#if 0

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices,int fee) {
        int res = 0;
        int n = prices.size();
        vector<vector<int>> a(n,vector<int>(2));
        a[0][0] = -prices[0];
        a[0][1] = 0;
        //1 2 3 0 2
        for(int i=1;i< prices.size();++i)
        {

            a[i][1] = max(a[i-1][1],prices[i]+a[i-1][0]-fee);
            a[i][0] = max(a[i-1][0],a[i-1][1]-prices[i]);

        }



        return max(a[n-1][1],a[n-1][0]);

    }
};


int main() {
    Solution s;
    vector<int> v1{1,3,2,8,4,9};
    vector<int> v2{1,3,7,5,10,3};
    vector<int> v3{4,5,2,4,3,3,1,2,5,4};

    cout << s.maxProfit(v1,2) << endl;
    cout << s.maxProfit(v2,3) << endl;
    cout << s.maxProfit(v3,1) << endl;


    return 0;
}


#endif



