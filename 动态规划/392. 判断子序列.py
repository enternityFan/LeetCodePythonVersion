# @Time : 2022-07-28 8:27
# @Author : Phalange
# @File : 392. 判断子序列.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0 or len(t) == 0:
            return True
        arr = [[0]*len(t)] * len(s)
        idx = 0
        for i in range(len(s)):
            flag = 0
            for j in range(idx,len(t)):
                if s[i] == t[j] and flag == 0:
                    if i == 0:
                        arr[i][j] = 1
                    else:
                        arr[i][j] =arr[i-1][j] +1
                    idx = j+1
                    flag = 1
                elif flag == 1:
                    arr[i][j] = arr[i][j-1]



        return arr[-1][-1] == len(s)








s = Solution()
print(s.isSubsequence("aaaaaa","bbaaaa"))