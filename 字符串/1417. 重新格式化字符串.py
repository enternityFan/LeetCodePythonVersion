# @Time : 2022-08-11 21:10
# @Author : Phalange
# @File : 1417. 重新格式化字符串.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D


class Solution:
    def reformat(self, s: str) -> str:
        nums = ""
        chars = ""
        for c in s:
            if c >='a' and c <='z':
                chars +=c
            else:
                nums +=c
        if abs(len(chars) - len(nums)) >1 or (chars == "" and nums == ""):
            return ""

        result = ""
        la = len(nums)
        lb = len(chars)
        i = 0
        j = 0
        while i <la  and j < lb:
            if la <= lb:
                result +=chars[j]
                result +=nums[i]
            else:
                result +=nums[i]
                result +=chars[j]
            i +=1
            j +=1
        while i < la:
            result  +=nums[i]
            i +=1
        while j < lb:
            result += chars[j]
            j +=1


        return result

print(Solution().reformat("covid2019"))