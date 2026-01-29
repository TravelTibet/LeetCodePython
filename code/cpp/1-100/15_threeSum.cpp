#include <bits/stdc++.h>
using namespace std;
//题目
//给你一个整数数组 nums ，判断是否存在三元组[nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。
//请你返回所有和为 0 且不重复的三元组。
//
//注意：答案中不可以包含重复的三元组。

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        std::sort(nums.begin(), nums.end(), [](int num1, int num2)
            {
                return num1 < num2;
            });
        vector<vector<int>> res;
        int nNums = nums.size();
        if (nNums < 3) return res;

        int nSum = 0;
        int nLeft = 0, nRight = 0;
        for (int i = 0; i < nNums - 1; ++i)
        {
            if (nums[i] > 0) break;//不可能有结果了
            while ((i+1) < (nNums - 1) && nums[i] == nums[i+1])
            {
                ++i;
            }
            
            nLeft = i + 1;
            nRight = nNums - 1;
            while (nLeft < nRight)
            {
                nSum = nums[i] + nums[nRight] + nums[nLeft];
                if (nSum == 0)
                {
                    vector<int> tempRes = { nums[i],nums[nRight],nums[nLeft] };
                    res.emplace_back(tempRes);
                    while (nLeft < nRight && nums[nLeft] == nums[nLeft + 1]){
                        ++nLeft;
                    }
                    while (nLeft < nRight && nums[nRight] == nums[nRight - 1]) {
                        --nRight;
                    }
                    ++nLeft;
                }
                else if (nSum < 0)
                {
                    ++nLeft;
                }
                else if (nSum > 0)
                {
                    --nRight;
                }
                
            }
        }
        return res;
    }
};

int main()
{
    Solution S;
    vector<int> nums = { -1,0,1,2,-1,-4 };
    auto vectors = S.threeSum(nums);
    for (auto& vector : vectors)
    {
        cout << "[";
        for (int n : vector)
        {
            cout << n << " ";
        }
        cout << "]\n";
    }
    return 0;
}