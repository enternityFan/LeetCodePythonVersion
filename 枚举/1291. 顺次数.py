# @Time : 2022-09-14 21:26
# @Author : Phalange
# @File : 1291. 顺次数.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import math
from typing import List
"""
100 100000
123
234
345
456
678
789
1234

"""

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        low_length = int(math.log10(low))+1
        high_length = int(math.log10(high))+1
        init_val = eval("".join([str(i) for i in range(1,low_length+1)]))
        val = init_val
        length = low_length
        while val <= high:
            if val >= low:
                ans.append(val)

            val += eval("1" * length)
            if str(val)[-1] <= str(val)[-2]:
                #说明要进位了
                length +=1
                val = eval(str(init_val) + str(length))
                init_val = val
        return ans




print(Solution().sequentialDigits(100,200000))