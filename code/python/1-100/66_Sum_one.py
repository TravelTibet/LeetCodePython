# author: Xiname
# -*- coding: utf-8 -*-
# @Time : 2023/12/20 10:14
# @File ：66_Sum_one.py
# @IDE ：PyCharm
# 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 定义一个字符空串
        number = ''
        # range（x）产生列表的范围是【0，x)，包括0不包括x
        for i in range(len(digits)):
            number += str(digits[i])
        # 把 number 转成整形然后再加一
        number = int(number) + 1
        # 把整形数按位先倒叙存入新列表
        str_number = str(number)
        new_list = [int(i) for i in str_number]
        # 上面是简写形式，与下面注释等价：
        # new_list = []
        # for i in str_number:
        #     new_list.append(int(i))
        return new_list


s = Solution()
print(s.plusOne([1, 2, 9]))
