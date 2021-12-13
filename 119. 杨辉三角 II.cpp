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
    vector<int> getRow(int rowIndex) {
        vector<vector<int>> v{{1},{1,1}};


        for(int i=2;i<=rowIndex;++i)
        {
            vector<int> temp{1};
            for(int j=1;j<=i-1;++j)
                temp.push_back(v[i-1][j-1]+v[i-1][j]);
            temp.push_back(1);
            v.push_back(temp);
        }

        return v[rowIndex];
    }
};



int main()
{
    Solution s;
    vector<vector<int>> v;





    return 0;

}


#endif


