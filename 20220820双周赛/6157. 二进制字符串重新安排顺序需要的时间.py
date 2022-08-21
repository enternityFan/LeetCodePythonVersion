# @Time : 2022-08-20 23:09
# @Author : Phalange
# @File : 6157. 二进制字符串重新安排顺序需要的时间.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:

        sec = 0
        idx = s.find("01")
        while idx !=-1:
            s = s.replace("01","10")
            idx = s.find("01")
            sec +=1
        return sec