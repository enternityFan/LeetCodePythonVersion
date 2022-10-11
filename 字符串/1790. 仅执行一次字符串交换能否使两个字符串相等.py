# @Time : 2022-10-11 14:28
# @Author : Phalange
# @File : 1790. 仅执行一次字符串交换能否使两个字符串相等.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D




class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diffidx = []
        for idx in range(len(s1)):
            if s1[idx] !=s2[idx]:
                diffidx.append(idx)

        if len(diffidx) == 2 and s1[diffidx[0]] == s2[diffidx[1]] and s2[diffidx[0]] == s1[diffidx[1]]:
            return True
        if diffidx == []:
            return True
        return False