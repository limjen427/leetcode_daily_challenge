class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(x, y, grid):
            queue = collections.deque()
            queue.append((x,y))
            
            while queue:
                cur_x, cur_y = queue.popleft()
                
                directions = [(0,-1), (0, 1), (-1, 0), (1, 0)]
                for direction in directions:
                    new_x, new_y = cur_x + direction[0], cur_y + direction[1]
                    if -1 < new_x < len(grid) and -1 < new_y < len(grid[0]):
                        if grid[new_x][new_y] == "1":
                            queue.append((new_x, new_y))
                            grid[new_x][new_y] = 0
            
        
        num_island = 0
        
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    grid[i][j] = 0
                    bfs(i, j, grid)
                    num_island += 1
        return num_island