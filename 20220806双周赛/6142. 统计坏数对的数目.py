# @Time : 2022-08-06 22:34
# @Author : Phalange
# @File : 6142. 统计坏数对的数目.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections
from typing import List


class Solution:

    def countBadPairs(self, nums: List[int]) -> int:
        """
        如果 nums[j] <= nums[i]，那么一定是坏数对
        1.首先，扫描一遍nums，记录一下对于nums[j]，i<j时nums[i]>=nums[j]的个数，这些都是坏数对
        2.在扫描的过程中，维护一个列表，记录了他前面哪个比他大。

        上面思路作废
        其实这个题可以变形为,j - nums[j] != i - nums[i]的数目，再变形为
        nums[j] - j != nums[i] - i 的数目
        :param nums:
        :return:
        """

        n = len(nums)
        if n == 1:
            return 0
        ans = 0
        # 首先都先减去下标
        # 然后我统计得到的结果都为0的，那么他们就可以互相组为好数对
        good = 0
        mydict = collections.defaultdict(int)
        for i in range(n):
            nums[i] -=i
            mydict[nums[i]] +=1
        for key,val in mydict.items():
            if val >=2: # 可以组成数对嘛
                good +=(val - 1) * val // 2

        ans = (n-1)*n // 2 - good

        return ans

print(Solution().countBadPairs([4,1,3,3]))
print(Solution().countBadPairs([1,2,3,4,5]))

