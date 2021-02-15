from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result: List[str] = []
        self.dfs(result, [], n, n)
        return result


    def dfs(self, result: List[str], prev: List[str], left: int, right: int):
        if left == right == 0:
            result.append(''.join(prev))
            return
        if left > 0:
            next = [*prev, '(']
            self.dfs(result, next, left - 1, right)
        if right > left:
            next = [*prev, ')']
            self.dfs(result, next, left, right - 1)


if __name__ == '__main__':
    print(Solution().generateParenthesis(3))