# author: Xiname
# -*- coding: utf-8 -*-
# @Time : 2023/12/22 9:29
# @File ：108sortedArrayToBST.py
# @IDE ：PyCharm

# 给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。
# 高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


s = Solution()
print(s.sortedArrayToBST([-10, -3, 0, 5, 9]))
