class Solution(object):
    def rotateGrid(self, grid, k):
        m, n = len(grid), len(grid[0])
        num_layers = min(m, n) // 2
        
        for d in range(num_layers):
            # 1. Extract the layer in CCW order
            layer = []
            # Top
            for j in range(d, n - d):
                layer.append(grid[d][j])
            # Right
            for i in range(d + 1, m - d):
                layer.append(grid[i][n - 1 - d])
            # Bottom
            for j in range(n - 2 - d, d - 1, -1):
                layer.append(grid[m - 1 - d][j])
            # Left
            for i in range(m - 2 - d, d, -1):
                layer.append(grid[i][d])
            
            # 2. Rotate the linear list
            L = len(layer)
            rot = k % L
            rotated_layer = layer[rot:] + layer[:rot]
            
            # 3. Put elements back into the grid in the same CCW order
            idx = 0
            # Top
            for j in range(d, n - d):
                grid[d][j] = rotated_layer[idx]
                idx += 1
            # Right
            for i in range(d + 1, m - d):
                grid[i][n - 1 - d] = rotated_layer[idx]
                idx += 1
            # Bottom
            for j in range(n - 2 - d, d - 1, -1):
                grid[m - 1 - d][j] = rotated_layer[idx]
                idx += 1
            # Left
            for i in range(m - 2 - d, d, -1):
                grid[i][d] = rotated_layer[idx]
                idx += 1
                
        return grid