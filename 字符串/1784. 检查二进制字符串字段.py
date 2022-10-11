# @Time : 2022-10-03 19:12
# @Author : Phalange
# @File : 1784. 检查二进制字符串字段.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        ans = True

        tmp = ""
        prev = None
        flag = 0

        if len(s) == 1:
            return True
        for i in range(1,len(s)):
            if s[i] == "1" and s[i-1]=="0":
                return False

        return True