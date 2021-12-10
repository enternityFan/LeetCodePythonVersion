


#if 1

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(prices.empty())
            return 0;

        int n = prices.size();
        vector<vector<int>> f(n,vector<int>(3));
        f[0][0] = -prices[0];
        for(int i=1;i<n;++i)
        {
            f[i][0] = max(f[i - 1][0],f[i-1][2] - prices[i]);
            f[i][1] = f[i-1][0] + prices[i];
            f[i][2] = max(f[i-1][1],f[i-1][2]);
        }
       return max(f[n-1][1],f[n-1][2]);



//            // 断开了
//            if(prices[i] - prices[minLeft] < tempRes)
//            {
//
//                if( tempCold!=-9999 && prices[i] - prices[minLeft] >0)
//                {
//                    //也就是说前面断过一次了
//                    //这次就开始认真的判断该在那断开了
//                    if(prices[tempCold-1] - prices[tempCold-2] < prices[tempCold+1]-prices[tempCold])
//                    {
//                        tempCold = tempCold - 1; // 这个时候就换个地方断开,并且更新一下结果
//                        res +=prices[tempCold-2];
//                        res -=prices[tempCold-1];
//
//                    }
//                    else
//                    {
//                        res -=prices[tempCold+1];
//                        res +=prices[tempCold];
//                    }
//                }
//
//
//                lastLeft = min(lastLeft,minLeft);
//                minLeft = i;
//                tempCold = i; // 存储一下断开的位置
//                res +=tempRes;
//                tempRes = 0;
//            }
//            else
//            {
//                lastRes = prices[i] - prices[lastLeft];
//                tempRes = prices[i] - prices[minLeft];
//            }
//
//
//        }
//        res =res + tempRes;


        return res;

    }
};


int main() {
    Solution s;
    vector<int> v1{7,1,5,3,6,4};
    vector<int> v2{7,6,4,3,1};
    vector<int> v3{};

    cout << s.maxProfit(v1) << endl;
    cout << s.maxProfit(v2) << endl;
    cout << s.maxProfit(v3) << endl;


    return 0;
}


#endif



