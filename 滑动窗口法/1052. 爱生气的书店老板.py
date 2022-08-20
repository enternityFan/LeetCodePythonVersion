# @Time : 2022-08-20 10:44
# @Author : Phalange
# @File : 1052. 爱生气的书店老板.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        ans = 0
        st = 0
        ed = st + minutes-1
        n = len(grumpy)
        # 首先查看老板要控制哪一阵不生气
        maxVal = 0#存放的是豁免的1的
        if minutes >= n:
            return sum(customers)
        for i in range(minutes):
            if grumpy[i] == 1:
                maxVal +=customers[i]
        val = maxVal
        while ed <n:
            ed+=1
            st+=1
            if ed !=n:
                val =val+(grumpy[ed]*customers[ed]-grumpy[st-1]*customers[st-1])
                maxVal = max(maxVal,val)


        #这里我就得到了
        for i in range(n):
            if grumpy[i] == 0:
                ans +=customers[i]
        return ans + maxVal


customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]

minutes = 3
print(Solution().maxSatisfied(customers,grumpy,minutes))