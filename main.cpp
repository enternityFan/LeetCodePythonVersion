


#if 0

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxScoreSightseeingPair(vector<int>& values) {
        int res = 0;
        int mx = values[0] + 0;

        for(int j=1;j<values.size();++j)
        {
            res = max(res,mx+values[j] - j);
            mx = max(mx,values[j]+j);
        }
        return res;
    }
};


int main() {
    Solution s;
    vector<int> v1{8,1,5,2,6};
    vector<int> v2{2,7,7,2,1,7,10,4,3,3};
    cout << s.maxScoreSightseeingPair(v1) << endl;
    cout << s.maxScoreSightseeingPair(v2) << endl;
    return 0;
}


#endif