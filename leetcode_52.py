from typing import List, Set


class Solution:
    def totalNQueens(self, n: int) -> int:
        # def dfs(state: List[int], xy_dif: List[int], xy_sum: List[int]) -> int:
        #     i = len(state)
        #     if i == n:
        #         return 1
        #     count = 0
        #     for j in range(n):
        #         if j not in state and i - j not in xy_dif and i + j not in xy_sum:
        #             count += dfs([*state, j], [*xy_dif, i - j], [*xy_sum, i + j])
        #     return count
        # return dfs([], [], [])

        def dfs(state: List[int], columns: Set[int], xy_dif: Set[int], xy_sum: Set[int]):
            row = len(state)
            if len(state) >= n:
                return 1
            count = 0
            for col in range(n):
                if col in columns or row - col in xy_dif or row + col in xy_sum:
                    continue
                
                columns.add(col)
                xy_dif.add(row - col)
                xy_sum.add(row + col)
                
                count += dfs([*state, col], columns, xy_dif, xy_sum)
                
                columns.remove(col)
                xy_dif.remove(row - col)
                xy_sum.remove(row + col)
            return count
        return dfs([], set(), set(), set())


if __name__ == "__main__":
    print(Solution().totalNQueens(1))
    print(Solution().totalNQueens(4))
