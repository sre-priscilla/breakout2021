from typing import List, Set


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # def dfs(results: List[List[int]], row: int, state: List[int], columns: Set[int], xy_dif: Set[int], xy_sum: Set[int]):
        #     if row >= n:
        #         results.append(state)
        #         return
        #     for col in range(n):
        #         if col in columns or row - col in xy_dif or row + col in xy_sum:
        #             continue
                
        #         columns.add(col)
        #         xy_dif.add(row - col)
        #         xy_sum.add(row + col)
                
        #         dfs(results, row + 1, [*state, col], columns, xy_dif, xy_sum)
                
        #         columns.remove(col)
        #         xy_dif.remove(row - col)
        #         xy_sum.remove(row + col)

        # results: List[List[int]] = []
        # dfs(results, 0, [], set(), set(), set())
        # return [['.' * i + 'Q' +  '.' * (n - i - 1) for i in result] for result in results]

        # def dfs(results: List[List[int]], state: List[int], xy_dif: List[int], xy_sum: List[int]):
        #     i = len(state)
        #     if i == n:
        #         results.append(state)
        #         return
        #     for j in range(n):
        #         if j not in state and i - j not in xy_dif and i + j not in xy_sum:
        #             dfs(results, [*state, j], [*xy_dif, i - j], [*xy_sum, i + j])
        # results: List[List[int]] = []
        # dfs(results, [], [], [])
        # fill = lambda p: ''.join(['Q' if i == p else '.' for i in range(n)])
        # return [[fill(place) for place in result] for result in results]

        def dfs(results: List[List[int]], state: List[int], columns: Set[int], xy_dif: Set[int], xy_sum: Set[int]):
            row = len(state)
            if row >= n:
                results.append(state)
                return
            for col in range(n):
                if col in columns or row - col in xy_dif or row + col in xy_sum:
                    continue
                
                columns.add(col)
                xy_dif.add(row - col)
                xy_sum.add(row + col)
                
                dfs(results, [*state, col], columns, xy_dif, xy_sum)
                
                columns.remove(col)
                xy_dif.remove(row - col)
                xy_sum.remove(row + col)

        results: List[List[int]] = []
        dfs(results, [], set(), set(), set())
        fill = lambda p: ''.join(['Q' if i == p else '.' for i in range(n)])
        return [[fill(place) for place in result] for result in results]


if __name__ == '__main__':
    print(Solution().solveNQueens(1))
    print(Solution().solveNQueens(4))
