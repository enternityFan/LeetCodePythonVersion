#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：29. 两数相除.py
@Author ：HuntingGame
@Date ：2023-02-02 10:06 
C'est la vie!!! enjoy ur day :D
'''

# TODO 这个代码有问题，参考思路就行，思路没有问题，就是java平台的代码没法在ptyhon的用。
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        这个和下面的加减乘除相比，会复杂很多，需要判断一下是不是负数
        因为系统最小的绝对值(-2 **31)比系统最大的绝对值要多1个(2 ** 31 -1 )
        1)如果a，b都是系统最小，那就返回1
        2)a不是系统最小，但b是，那就返回0，因为除数很大
        3)a,b都不是系统最小，那就用绝对值去算
        4)a是系统最小，b是，那就很麻烦
        :param dividend:
        :param divisor:
        :return:
        """
        if divisor == -2 ** 31:
            return True if dividend == -2 ** 31 else False

        #代码能到这里说明除数不是系统最小
        if dividend == -2 ** 31:
            if divisor == self.negNum(1):
                # 如果除数是-1，系统最小除-1是溢出的，所以返回系统最大。
                return 2 ** 31 - 1
            """
            下面两行代码，举个例子，比如a是系统最小，是-10，我们认为-10就是系统最小，那么9就是系统最大，模拟系统最小的绝对值比系统最大的绝对值大。
            如果b是2，那么第一行代码就是在做：(-10+1)/2 = -4,但是很明显-10/2要等于-5的，中间因为小数被截断了有误差，
            那么就让-10 - (-4 * 2)=-2,然后再-2 / 2 = -1,给加到-4上，就是-5，弥补了这个误差。
            
            """
            res = self.div(self.add(dividend, 1), divisor)  #为了计算被除数是系统最小，这里首先给他加1，然后算
            return self.add(res, self.div(self.minus(dividend, self.multi(res, divisor)), divisor))#这里呢把前面算的结果加一个系统最小减去前面的结果*除数的结果再除以2给加上去

        # dividend不是系统最大，也不是最小。
        return self.div(dividend, divisor)
    def add(self,a,b):
        """
        注意ab都要大于0.
        两数相与再往左移动一位，是一个进位的信息；
        两个数相异或，是两个数无进位相加的结果
        然后把这两个结果再算异或和与的左移，直到进位的信息都消失，就是最终的结果
        :param a:
        :param b:
        :return:
        """
        sum = a

        while b:
            a, b = (a ^ b) & 0xFFFFFFFF, (a & b) << 1

        if a >> 31 == 0:
            return a
        else:
            return a - 2 ** 32


    def negNum(self,n):
        """
        求相反数，其实就是b取反加1
        :param n:
        :return:
        """
        return self.add(~n,1)

    def minus(self,a,b):
        """
        两数相减，其实就是a加上b的相反数
        :param a:
        :param b:
        :return:
        """
        return self.add(a, self.negNum(b))

    def multi(self,a,b):
        """

        实现乘法。
        其实就是b的每一个二进制位和a的乘，然后再求一个和。
        这个的话，就是a左移0位，b向右移动0位，看b最后一位是不是1，如果是，就加到res里；
        第二步就a左移1位，b右移动1位，重复上面的直到b为0
        :param a:
        :param b:
        :return:
        """
        res = 0
        while b !=0:
            if (b & 1) !=0:
                res = self.add(res,a)

            a <<=1
            b >>=1
        return res

    def isNeg(self,a):
        """
        判断是不是负数
        :param a:
        :return:
        """
        return a < 0

    def div(self, a, b):
        """
        需要保证a b都不是系统最小。
        让b左移，看什么时候最接近a但又不超过a，那么把a减去这个数，
        然后再拿这个结果，当a，重复上面的过程
        对于a*b,其实在模拟 a = b * 2^3 + b * 2^1..类似的效果。
        a/b的话，就是 a = b * 2^甲 + b* 2^乙类似的，甲乙这就是b每次位移的位数
        :param a:
        :param b:
        :return:
        """
        x = self.negNum(a) if self.isNeg(a) else a
        y = self.negNum(b) if self.isNeg(b) else b
        res = 0
        i = 31#这里直接暴力尝试31个位，而不是上面写的那样。
        while i > self.negNum(1):
            if (x >> i) >=y:
                res |= 1 << i
                x = self.minus(x,y << i)
            #print(i)

            i = self.minus(i,1)

        return self.negNum(res) if self.isNeg(a) ^ self.isNeg(b) else res #这个异或是判断符号是不是一样的，ab





print(Solution().minus(10,-3))
print(Solution().divide(-2147483648,-3))

