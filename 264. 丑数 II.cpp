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
    int nthUglyNumber(int n) {

      vector<int> ugly(n,1),idx(3,0);


        for(int i=1;i<n;++i)
        {
            int a = ugly[idx[0]]*2,b=ugly[idx[1]]*3,c=ugly[idx[2]]*5;
            int next = min(a,min(b,c));
            if(next == a){
                ++idx[0];
            }
            if(next == b){
                ++idx[1];

            }
            if(next == c){
                ++idx[2];
            }
            ugly[i] = next;



        }

    return ugly[ugly.size() - 1];

    }
};

int main()
{
    Solution s;
    vector<int> v1{1,2,3,4,5,6};
    vector<int> v2{7,7,7,7};
    vector<int> v3{3,-1,-5,-9};
    cout << s.nthUglyNumber(10) << endl;





    return 0;

}


#endif
//
// Created by lifan on 2021/12/11.
//

//
// Created by lifan on 2021/12/12.
//

