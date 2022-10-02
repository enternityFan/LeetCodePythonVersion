# @Time : 2022-10-01 21:52
# @Author : Phalange
# @File : 1694. 重新格式化电话号码.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(" ","").replace("-","")
        ans = ""
        i = 0
        while i <len(number):
            tmp = len(number ) - i
            if tmp<=4:
                if tmp == 4:
                    ans +=number[i:i+2] + "-" + number[i+2:]
                else:
                    ans +=number[i:]
                break


            else:

                ans +=number[i:i+3] + "-"
                i +=3
        return ans

print(Solution().reformatNumber("12376"))