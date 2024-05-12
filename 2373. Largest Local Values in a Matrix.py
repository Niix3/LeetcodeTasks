# You are given an n x n integer matrix grid.
#
# Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:
#
# maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
# In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.
#
# Return the generated matrix.

class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)
        new_len = n-2
        def get_max(i,j):
            max_elem = grid[i][j]
            for a in range(i,i+3):
                for b in range(j,j+3):
                    max_elem = max(max_elem, grid[a][b])
            return max_elem
        new_grid = []
        for k in range(new_len):
            new_grid.append([])
        for i in range(new_len):
            for j in range(new_len):
                new_grid[i].append(get_max(i,j))
        return new_grid


s = Solution()
print(s.largestLocal(grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]))
