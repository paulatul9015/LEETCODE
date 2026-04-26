class Solution(object):
    def containsCycle(self, grid):
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c, pr, pc, value):
            visited.add((r, c))
            
            # Directions: Up, Down, Left, Right
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                
                # Check boundaries and matching value
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == value:
                    # If visited and not the parent, cycle found!
                    if (nr, nc) in visited:
                        if (nr, nc) != (pr, pc):
                            return True
                    else:
                        if dfs(nr, nc, r, c, value):
                            return True
            return False

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited:
                    # Start DFS for unvisited components
                    if dfs(r, c, -1, -1, grid[r][c]):
                        return True
        return False