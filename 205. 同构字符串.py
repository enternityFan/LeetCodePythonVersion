# @Time : 2022-07-28 8:08
# @Author : Phalange
# @File : 205. 同构字符串.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        return len(set(s)) == len(set(t)) == len(set(zip(s,t)))






s = Solution()
print(s.isIsomorphic("foo","a2d"))