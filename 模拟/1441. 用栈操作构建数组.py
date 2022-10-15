# @Time : 2022-10-15 8:11
# @Author : Phalange
# @File : 1441. 用栈操作构建数组.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        mylist = list(range(1,n+1))
        ans = []
        p1 = 0
        i = 0
        while i < len(target):
            if target[i] == mylist[p1]:
                p1 +=1
                ans.append("Push")
                i +=1
            else:
                pred_p1 = p1
                while target[i] !=mylist[p1]:
                    p1 +=1
                    ans.append("Push")
                for _ in range(p1 - pred_p1):
                    ans.append("Pop")

        return ans

print(Solution().buildArray([1,3],3))




