class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])
        
        # Mapping street type to (dr, dc) directions it connects
        # Directions: (row_offset, col_offset)
        # Up: (-1, 0), Down: (1, 0), Left: (0, -1), Right: (0, 1)
        directions = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }
        
        visited = set([(0, 0)])
        queue = [(0, 0)]
        
        while queue:
            r, c = queue.pop(0)
            if r == m - 1 and c == n - 1:
                return True
            
            for dr, dc in directions[grid[r][c]]:
                nr, nc = r + dr, c + dc
                
                # Check boundaries and if already visited
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    # Check if the neighbor can connect back to current cell
                    # To connect back, the neighbor must have a direction that is (-dr, -dc)
                    if (-dr, -dc) in directions[grid[nr][nc]]:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
                        
        return False