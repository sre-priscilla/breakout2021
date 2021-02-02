from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority, count = nums[0], 0
        for x in nums:
            if count == 0:
                majority = x
            if x == majority:
                count += 1
            else:
                count -= 1
        return majority


if __name__ == '__main__':
    print(Solution().majorityElement([3, 2, 3]))
    print(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]))
