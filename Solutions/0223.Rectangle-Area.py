223. Rectangle Area

Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area

Example:

Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45


class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        if not self.overlap(A, B, C, D, E, F, G, H):
            return (C-A)*(D-B) + (G-E)*(H-F)
        else:
            return (C-A)*(D-B) + (G-E)*(H-F) - abs((min(H, D)-max(B, F))*(min(C, G)-max(E, A)))
        
    def overlap(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> bool:
        if D <= F or C <= E or A >= G or B >= H:
            return False
        return True
