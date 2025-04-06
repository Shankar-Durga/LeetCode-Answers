class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def checker(row,col):
            grid[row][col] = 0
            directions = [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]
            for r,c in directions:
                if r>=0 and c>=0 and r<len(grid) and c<len(grid[0]) and grid[r][c] == "1":
                    checker(r,c)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    print(count)
                    count +=1
                    checker(i,j)
        return count