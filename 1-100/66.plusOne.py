# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 xiname All Rights Reserved 
#
# @Time    : 2024/12/4 10:18
# @Author  : xiname
# @File    : 66.plusOne.py
# @IDE     : PyCharm
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
