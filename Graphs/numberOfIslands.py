'''
Leetcode #200: Number of Islands
https://leetcode.com/problems/number-of-islands/
Time: O(n) | Space: O(n)
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islandCount = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (grid[row][col] == '1'):
                    islandCount += 1
                    self.terraform(row, col, grid)
        return islandCount

    def terraform(self, row, col, grid):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == "0":
            return

        grid[row][col] = "0"
        self.terraform(row, col + 1, grid)
        self.terraform(row, col - 1, grid)
        self.terraform(row + 1, col, grid)
        self.terraform(row - 1, col, grid)
