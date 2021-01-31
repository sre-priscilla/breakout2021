from typing import List


class Solution:
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     if len(nums) < 3:
    #         return []
    #     _set = set()
    #     for i, x in enumerate(nums):
    #         target, _map = -x, dict()
    #         for j, y in enumerate(nums):
    #             if i == j:
    #                 continue
    #             if y in _map:
    #                 group = (x, y, nums[_map[y]])
    #                 _set.add(tuple(sorted(group)))
    #             else:
    #                 _map[target - y] = j
    #     return list(_set)

    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     if len(nums) < 3:
    #         return []
    #     n, ret = len(nums), set()
    #     nums.sort()
    #     for i in range(n - 2):
    #         if i > 0 and nums[i] == nums[i - 1]:
    #             continue
    #         target, _map = -nums[i], dict()
    #         for j in range(i + 1, n):
    #             if nums[j] in _map:
    #                 ret.add((nums[i], _map[nums[j]], nums[j]))
    #             else:
    #                 _map[target - nums[j]] = nums[j]        
    #     return list(ret)

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        n, ret = len(nums), []
        nums.sort()
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s < 0:
                    j += 1
                elif s > 0:
                    k -= 1
                else:
                    ret.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j, k = j + 1, k - 1
        return ret


if __name__ == "__main__":
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
