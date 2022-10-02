# @Time : 2022-10-02 11:01
# @Author : Phalange
# @File : 6194. 最小 XOR.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        """
        1. num1,num2 1的个数相同->num1
        2. num1 1的个数比num2 1的个数多,这个时候最小就是把num1的高位给mask掉
        3. num1 1的个数比num2 1的个数少，这个时候，num应该尽量往低处排
        :param num1:
        :param num2:
        :return:
        """
        one1 = self.count_2(num1)
        one2 = self.count_2(num2)
        num = 0
        if one1 == one2:
            num = num1
        elif one1 > one2:
            tmp = 1
            while one1 !=one2:
                if num1 & tmp == tmp:
                    one1 -=1
                    num1 -=tmp
                tmp <<=1
            num = num1
        else:
            tmp = 1
            i = 0

            while i !=one2-one1:
                if num1 & tmp != tmp:
                    i +=1
                    num +=tmp
                tmp <<=1
            num +=num1




        return num


    def count_2(self,v):
        num = 0
        while v:
            num += v & 1
            v >>= 1
        return num

print(Solution().minimizeXor(79,74))