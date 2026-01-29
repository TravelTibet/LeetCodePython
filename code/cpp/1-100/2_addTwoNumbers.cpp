#include <bits/stdc++.h>
#include <Windows.h>

// 题目：
// 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
// 请你将两个数相加，并以相同形式返回一个表示和的链表。
// 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};

class Solution 
{
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2)
    {
        ListNode* result = new ListNode();
        ListNode* nextNode = result;

        bool bIsTen = false;
        while (l1 || l2)
        {
            ListNode* pTempNode = new ListNode();
            int nSum = 0;

            if (l1 && l2)
            {
                nSum = l1->val + l2->val;
            }
            else if (l1)
            {
                nSum = l1->val;
            }
            else if (l2)
            {
                nSum = l2->val;
            }

            nSum = bIsTen ? ++nSum : nSum;
            if (nSum >= 10)
            {
                bIsTen = true;
                nSum %= 10;
            }
            else
            {
                bIsTen = false;
            }
            pTempNode->val = nSum;

            nextNode->next = pTempNode;
            nextNode = pTempNode;

            if (l1) l1 = l1->next;
            if (l2) l2 = l2->next;
        }

        if (bIsTen)
        {
            nextNode->next = new ListNode(1);
        }
        return result->next;
    }
};

/*int main(void)
{
    Solution S;
    //ListNode* pList1 = new ListNode(2, new ListNode(6, new ListNode(9)));
    ListNode* pList1 = new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9))))));
    ListNode* pList2 = new ListNode(5, new ListNode(6, new ListNode(9)));
    ListNode* pResult = S.addTwoNumbers(pList1, pList2);
    if (pResult)
    {
        while (pResult)
        {
			std::cout << pResult->val << " ";
            pResult = pResult->next;
        }
    }

	return 0;
}*/