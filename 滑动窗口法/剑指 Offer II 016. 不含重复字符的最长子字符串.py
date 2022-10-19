# @Time : 2022-10-17 12:51
# @Author : Phalange
# @File : 剑指 Offer II 016. 不含重复字符的最长子字符串.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        n = len(s)
        mywindows = collections.defaultdict(int)
        st = 0
        ed = -1
        for i in range(n):
            if s[i] not in mywindows:
                mywindows[s[i]] = 1
                ed +=1
            else:
                ans = max(ans,ed-st+1)
                for k in range(st,ed+1):
                    mywindows[s[k]] = 0
                    if s[k] == s[i]:
                        st = k + 1
                        break
                ed +=1
        return max(ans,ed-st+1)

print(Solution().lengthOfLongestSubstring("abcabcbb"))


