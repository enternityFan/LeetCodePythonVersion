# @Time : 2022-08-13 15:34
# @Author : Phalange
# @File : 1387. 将整数按权重排序.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections
from functools import cmp_to_key


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:

        mymap = collections.defaultdict(int)
        nums = list(range(lo,hi+1))
        n = hi - lo + 1
        weights = []
        for i in range(n):
            cur = nums[i]
            time = 0
            path = [cur]#记录一下路径
            while cur !=1:
                if cur in mymap:
                    time = time + mymap[cur]
                    break
                if cur % 2 == 0:
                    cur = cur // 2
                else:
                    cur = 3*cur + 1
                path.append(cur)
                time +=1
            lpath = len(path)-1 # 不算最后的1
            for j in range(lpath):
                mymap[path[j]] =time - j


            weights.append(time)
        nums,weights = (list(t) for t in zip(*sorted(zip(nums, weights),key=lambda x:x[1] )))
        return nums[k-1]

print(Solution().getKth(12,15,2))
