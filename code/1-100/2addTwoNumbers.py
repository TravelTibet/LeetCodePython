"""
@Project ：LeetCodePython
@File    ：2addTwoNumbers.py
@IDE     ：PyCharm
@Author  ：XiName
@Date    ：2026/1/27 10:15
"""

# 题目：
# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。


from typing import Optional

from zope.interface.common import optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # 可视化输出列表用来调试
    def __str__(self):
        values = []
        cur = self
        while cur is not None:
            values.append(str(cur.val))
            cur = cur.next
        return " -> ".join(values)


class Solution:
    # 法一：先把数据存好然后再把10的拆开 pass

    # 法二：存进去的时候考虑是否大于10，然后特殊处理
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1, node2 = l1, l2

        result = ListNode()
        nextNode = result
        isBiggerThenTen = False  # 是否需要进位

        # 位数相同的时候
        while node1 is not None and node2 is not None:
            number1 = node1.val
            number2 = node2.val
            tempSum = number1 + number2
            if isBiggerThenTen:
                tempSum = tempSum + 1

            if tempSum >= 10:
                # 个位
                listNodeTen = ListNode(tempSum % 10)

                nextNode.next = listNodeTen
                nextNode = listNodeTen

                node1 = node1.next
                node2 = node2.next
                isBiggerThenTen = True
                continue
            else:
                isBiggerThenTen = False

            tempListNode = ListNode(tempSum)
            nextNode.next = tempListNode
            nextNode = tempListNode

            node1 = node1.next
            node2 = node2.next

        def oneNodeSum(node: Optional[ListNode]) -> Optional[ListNode]:
            nonlocal isBiggerThenTen, tempSum, listNodeTen, nextNode, tempListNode# 外部变量
            while node is not None:
                tempSum = node.val
                if isBiggerThenTen:
                    tempSum = tempSum + 1

                if tempSum >= 10:
                    # 个位
                    listNodeTen = ListNode(tempSum % 10)

                    nextNode.next = listNodeTen
                    nextNode = listNodeTen

                    node = node.next
                    isBiggerThenTen = True
                    continue
                else:
                    isBiggerThenTen = False

                tempListNode = ListNode(tempSum)
                nextNode.next = tempListNode
                nextNode = tempListNode

                node = node.next

        # l1比较长的时候
        oneNodeSum(node1)

        # l2比较长的时候
        oneNodeSum(node2)

        if isBiggerThenTen:  # 最后面的一个
            tempListNode = ListNode(1)
            nextNode.next = tempListNode

        result = result.next  # 去除最开始的0
        return result


if __name__ == '__main__':
    s = Solution()
    # list1 = ListNode(2, ListNode(6, ListNode(9)))
    list2 = ListNode(5, ListNode(6, ListNode(9)))
    list1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))  # 999999
    # list2 = ListNode(9, ListNode(9, ListNode(9)))  # 999

    resultList = s.addTwoNumbers(list1, list2)
    print(f'l1 is: {list1}', f'l2 is: {list2}', f'result is: {resultList}', sep='\n')
