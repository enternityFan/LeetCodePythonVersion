# @Time : 2022-08-06 22:46
# @Author : Phalange
# @File : 6174. 任务调度器 II.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections
from typing import List


class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        mydict = {} # 用来存放某个任务完成几天了
        ans = 0
        idx = 0
        n = len(tasks)
        while idx < n:
            cur = tasks[idx]
            if cur not in mydict or ans - mydict[cur] > space:
                mydict[cur] = ans # 更新为当前天

                # 不管上面两种情况的哪种，这一天都可以完成这个任务
                idx +=1
                ans +=1
            else:
                err = mydict[cur] + space - ans+1
                ans +=err

        return ans
print(Solution().taskSchedulerII([1,2,1,2,3,1],3))
print(Solution().taskSchedulerII([5,8,8,5],2))
print(Solution().taskSchedulerII([2]*10000,5))