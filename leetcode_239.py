from typing import List


class Solution:
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     win, ret = [], []
    #     if k == 0 or len(nums) == 0:
    #         return ret
    #     for i in range(k):
    #         while win and win[-1] < nums[i]:
    #             win.pop()
    #         win.append(nums[i])
    #     ret.append(win[0])
    #     for j in range(k, len(nums)):
    #         if win[0] == nums[j - k]:
    #             win.pop(0)
    #         while win and win[-1] < nums[j]:
    #             win.pop()
    #         win.append(nums[j])
    #         ret.append(win[0])
    #     return ret

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        win, ret = [], []
        for i, x in enumerate(nums):
            if i >= k and win[0] <= i - k:
                win.pop(0)
            while win and nums[win[-1]] <= x:
                win.pop()
            win.append(i)
            if i >= k - 1:
                ret.append(nums[win[0]])
        return ret




if __name__ == '__main__':
    a = [1, 2, 3]
    a.pop(0)
    print(a)