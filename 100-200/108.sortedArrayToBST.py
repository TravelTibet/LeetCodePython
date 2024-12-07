# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 xiname All Rights Reserved 
#
# @Time    : 2024/12/4 10:20
# @Author  : xiname
# @File    : 108.sortedArrayToBST.py
# @IDE     : PyCharm
from idlelib.tree import TreeNode
from typing import List


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> [TreeNode]:
        # 递归出口，判断nums是否为空,为空返回空结点
        if len(nums) == 0:
            return None
        mid = (len(nums) - 1) // 2
        root = TreeNode(nums[mid])
        # print('now_mid is :', nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root