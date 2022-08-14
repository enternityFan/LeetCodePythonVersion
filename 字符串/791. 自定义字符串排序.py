# @Time : 2022-08-14 14:31
# @Author : Phalange
# @File : 791. 自定义字符串排序.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections


class Solution:
    def customSortString(self, order: str, s: str) -> str:

        mycnt = collections.Counter(s)
        ans = ""
        for c in order:
            if c in mycnt:
                ans = ans + c * mycnt[c]
                mycnt.pop(c)
        for key,val in mycnt.items():
            ans = ans + key * val

        return ans

print(Solution().customSortString("cba","abcd"))