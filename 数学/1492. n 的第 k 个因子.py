# @Time : 2022-07-30 19:18
# @Author : Phalange
# @File : 1492. n 的第 k 个因子.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        res = []
        idx = 0#记录有多个因子了
        for i in range(1,n+1):
            if n % i ==0:

                res.append(i)
                idx += 1
                if idx == k:
                    return res[idx-1]


        return -1

print(Solution().kthFactor(12,3))