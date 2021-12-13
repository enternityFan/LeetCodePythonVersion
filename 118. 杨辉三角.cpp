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
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> v{{1}};

        if (numRows == 1 )
            return v;
        v.push_back(vector<int>{1,1});
        if(numRows ==2)
            return v;
        for(int i=2;i<numRows;++i)
        {
            vector<int> temp{1};
            for(int j=1;j<=i-1;++j)
                temp.push_back(v[i-1][j-1]+v[i-1][j]);
            temp.push_back(1);
            v.push_back(temp);
        }

        return v;


    }
};



int main()
{
    Solution s;
    vector<vector<int>> v;
    v = s.generate(5);




    return 0;

}


#endif

