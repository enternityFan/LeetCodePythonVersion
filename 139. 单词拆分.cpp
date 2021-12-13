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
    bool wordBreak(string s, vector<string>& wordDict) {

        auto wordDictSet = unordered_set<string>();
        for(auto word:wordDict)
            wordDictSet.insert(word);

        auto dp = vector<bool> (s.size() + 1);
        dp[0] = true;
        for(int i=1;i<=s.size();++i){
            for(int j=0;j<i;++j){
                if(dp[j] && wordDictSet.find(s.substr(j,i-j))!=wordDictSet.end()){
                    dp[i] = true;
                    break;
                }
            }
        }


       return dp[s.size()];
    }
};


int main()
{
    Solution s;
    vector<string> v{"leet", "code"};
    vector<string> v1{"cats","dog","and","sand","cat"}; // catsandog
    vector<string> v2{"aaa","aaaa"};
    cout << s.wordBreak("aaaaaaa",v2) << endl;




    return 0;

}


#endif
