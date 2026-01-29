# author: Xiname
# -*- coding: utf-8 -*-
# @Time : 2023/12/20 11:35
# @File ：88_Merge_two_sorted_array.py
# @IDE ：PyCharm
# 给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。
# 请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。
# 注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。
# 为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。
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
        # print(nums1)


s = Solution()
s.merge(nums1 = [0], m = 0, nums2 = [1], n = 1)
