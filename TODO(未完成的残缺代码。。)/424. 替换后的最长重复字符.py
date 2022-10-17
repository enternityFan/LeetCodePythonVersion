# @Time : 2022-10-17 12:27
# @Author : Phalange
# @File : 424. 替换后的最长重复字符.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        mywindows = collections.defaultdict(int)
        mywindows[s[0]] = 1
        n = len(s)
        st = 0
        e = 0
        ans = 0
        elem = s[0]
        for i in range(1,n):
            if s[i] ==elem:
                mywindows[s[i]] +=1

                e +=1
            elif sum(mywindows.values()) - mywindows[elem] < k:
                mywindows[s[i]] +=1
                elem = s[i] if mywindows[s[i]] > mywindows[elem] else elem

                e +=1
            else:
                ans = max(ans,e-st+1)

                mywindows[s[i]] += 1 #先加进来,现在有K+1个不相等的
                e +=1
                for j in range(st,e):
                    mywindows[s[j]] -=1
                    if mywindows[s[j]] == 0 :
                        mywindows.pop(s[j])
                        st =j+1

                        break
                elem = max(mywindows,key=mywindows.get)

        return max(ans,e-st+1)
s = "EQQEJDOBDPDPFPEIAQLQGDNIRDDGEHJIORMJPKGPLCPDFMIGHJNIIRSDSBRNJNROBALNSHCRFBASTLRMENCCIBJLGAITBFCSMPRO"

print(Solution().characterReplacement(s,2))
