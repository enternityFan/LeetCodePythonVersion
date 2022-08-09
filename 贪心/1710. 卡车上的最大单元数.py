# @Time : 2022-08-09 17:19
# @Author : Phalange
# @File : 1710. 卡车上的最大单元数.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1],reverse=True)
        ans = 0
        tmp = 0 # 当前选择了多少个箱子
        for each in boxTypes:
            if tmp+each[0] <truckSize:
                ans +=each[1]*each[0]
                tmp +=each[0]
            elif tmp < truckSize:
                for i in range(each[0]):
                    if tmp <truckSize:
                        ans +=each[1]
                        tmp +=1
                    else:
                        break
            else:
                break
        return ans


boxTypes = [[1,3],[2,2],[3,1]]
truckSize = 4
print(Solution().maximumUnits(boxTypes,truckSize))