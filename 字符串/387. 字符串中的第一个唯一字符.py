# @Time : 2022-09-04 19:22
# @Author : Phalange
# @File : 387. 字符串中的第一个唯一字符.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        mymap = collections.Counter(s)
        ans = 0
        flag = 0
        for c in s:
            if mymap[c] ==1:
                flag = 1
                break
            else:
                ans +=1
        return ans if flag else -1

print(Solution().firstUniqChar("helhlo"))