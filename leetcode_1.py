class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _map = dict()
        for i, x in enumerate(nums):
            if x in _map:
                return [_map[x], i]
            else:
                _map[target - x] = i
        return [-1, -1]
            