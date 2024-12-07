# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 xiname All Rights Reserved 
#
# @Time    : 2024/12/4 10:21
# @Author  : xiname
# @File    : 118.generate.py
# @IDE     : PyCharm
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        new_list = []
        # 其他情况：
        for numrow in range(1, numRows + 1):  # numrow 意思是行数
            # 特例
            if numrow == 1:
                new_list.append([1])
                continue
            if numrow == 2:
                new_list.append([1, 1])
                continue
            # print(f'new_list{new_list}')
            temp_list = [1]  # 每行第一个数都是1
            # 每一行应该有 n=numrow 个数
            for num in range(1, numrow - 1):  # 从1循环到numrow-2
                old_list = new_list[numrow - 2]  # 上一层的数组
                temp_list.append(old_list[num - 1] + old_list[num])

            temp_list.append(1)  # 添加最后一个元素
            new_list.append(temp_list)
        return new_list
