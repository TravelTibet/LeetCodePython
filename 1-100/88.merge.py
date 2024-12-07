# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 xiname All Rights Reserved 
#
# @Time    : 2024/12/4 10:19
# @Author  : xiname
# @File    : 88.merge.py
# @IDE     : PyCharm
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j = 0, 0
        num_temp = []
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                # num1不变，只需移动指针 i 即可
                num_temp.append(nums1[i])
                i += 1
            else:
                num_temp.append(nums2[j])
                j += 1
        # 把剩下的合并到num_temp里面
        while i < m:
            num_temp.append(nums1[i])
            i += 1
        while j < n:
            num_temp.append(nums2[j])
            j += 1
        # 保证nums1【：】还是原来的那个序列，进行序列的复制操作
        nums1[:] = num_temp