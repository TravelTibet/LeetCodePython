# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 xiname All Rights Reserved 
#
# @Time    : 2024/12/4 10:24
# @Author  : xiname
# @File    : 11.maxArea.py
# @IDE     : PyCharm
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 初始化两个指针 i=0, j=len(height)-1
        i, j = 0, len(height) - 1
        maxArea = 0
        while i != j:

            if height[i] < height[j]:
                min_height = height[i]
                # print('i = {}, j = {}'.format(i, j))
                i += 1
            else:
                min_height = height[j]
                # print('i = {}, j = {}'.format(i, j))
                j -= 1
            # 这里长度变成 j - i + 1 是因为前面会多减一个1，造成结果有问题！！！
            maxArea = max(maxArea, (j - i + 1) * min_height)
            # print('maxArea = {},min_height = {}'.format(maxArea, min_height), )
        return maxArea
