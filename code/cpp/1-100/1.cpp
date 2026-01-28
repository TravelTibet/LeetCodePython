#include <bits/stdc++.h>
// 题目
//给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
//
//你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
//
//你可以按任意顺序返回答案。

using namespace std;
class Solution
{
public:
    vector<int> twoSum(vector<int>& nums, int target) 
    {
		int nSize = nums.size();
        vector<int> res;
        for (int i = 0; i < nSize; ++i)
        {
            for (int j = i + 1; j < nSize; ++j)
            {
                int nRes = nums[i] + nums[j];
                if (nRes == target)
                {
                    res.push_back(i);
                    res.push_back(j);
                    break;
                }
            }
        }
        return res;
    }
};

//int main(void)
//{
//    Solution S;
//	vector<int> nums = { 2,7,11,15 };
//	auto res = S.twoSum(nums, 9);
//    cout << "Res:";
//    for (int nValue : res) {
//		cout << nValue << " ";
//    }
//    return 0;
//}