class Solution(object):
    def floodFill(self, image, sr, sc, color):
        rows, cols = len(image), len(image[0])
        original_color = image[sr][sc]
        
        # If the starting pixel is already the target color, no work is needed
        if original_color == color:
            return image
        
        def dfs(r, c):
            # Base case: check bounds and if the pixel matches the original color
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != original_color:
                return
            
            # Update the color
            image[r][c] = color
            
            # Recursively visit neighbors (Up, Down, Left, Right)
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        dfs(sr, sc)
        return image