from typing import List

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        row_count = [0] * m
        col_count = [0] * n
        position = {}

        # Map each value in mat to its position (row, column)
        for i in range(m):
            for j in range(n):
                position[mat[i][j]] = (i, j)

        for idx, value in enumerate(arr):
            row, col = position[value]
            row_count[row] += 1
            col_count[col] += 1

            # Check if the current row or column is completely painted
            if row_count[row] == n or col_count[col] == m:
                return idx

        return -1

# This Code is Contributed by Kalyan Babu Allamudi