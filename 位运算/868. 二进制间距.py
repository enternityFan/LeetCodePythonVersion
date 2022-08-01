# @Time : 2022-08-01 21:10
# @Author : Phalange
# @File : 868. 二进制间距.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import math


class Solution:
    def binaryGap(self, n: int) -> int:

        res = [0] # 用来存放结果
        rightOne = 0  #记录最右边1的位置
        while n!=0:
            if rightOne ==0:
                rightOne = n &(~n+1)
                res.append(0)
            else:
                if n&(~n+1) !=0:
                    res.append(int(math.log2(n&(~n+1)) - math.log2(rightOne)))
                else:
                    break
                rightOne = n & (~n+1) # 更新一下

            n ^=rightOne

        return max(res)

print(Solution().binaryGap(13))