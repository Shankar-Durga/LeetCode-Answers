class Solution:
    def island_checker(self, grid, row, col):
        grid[row][col] = 0
        lst = [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]
        for i, j in lst:
            if i>=0 and j>=0 and i<len(grid) and j<len(grid[0]):
                if grid[i][j] == "1":
                    self.island_checker(grid, i, j)

    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.island_checker(grid,i,j)
                    islands += 1
        return islands
