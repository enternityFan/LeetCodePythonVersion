# @Time : 2022-09-29 15:58
# @Author : Phalange
# @File : 面试题 01.09. 字符串轮转.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D




class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        if len(s1) !=len(s2):
            return False
        s2 +=s2
        if s2.find(s1) !=-1:
            return True
        return False



print(Solution().isFlipedString("PvcvpkpHwaXQxpgGzURBvHRMvCsCPPmlKBSzXDWSvrxLBPdAvRpgcIwNOVQDdwPIElrAFqmb","SvrxLBPdAvRpgcIwNOVQDdwPIElrAFqmbPvcvpkpHwaXQxpgGzURBvHRMvCsCPPmlKBSzXDW"))


