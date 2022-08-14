# @Time : 2022-08-14 12:36
# @Author : Phalange
# @File : 面试题 10.02. 变位词组.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        n = len(strs)
        tmp =[]
        for each in strs:
            tmp.append(dict(collections.Counter(each)))

        ans2 = []
        for i in range(n):
            if ans == []:
                ans.append([strs[i]])
                ans2.append(i)#记录0号索引
            else:
                flag = 0
                for j in range(len(ans)):
                    if tmp[i] == tmp[ans2[j]]:
                        ans[j].append(strs[i])
                        flag = 1
                        break
                if flag == 0:
                    #说明没找到
                    ans.append([strs[i]])
                    ans2.append(i)


        return ans


print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))