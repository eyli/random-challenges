# https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]):
            return image

        initialColor = image[sr][sc]
        if initialColor == color:
            return image

        self.floodFillHelper(image, sr, sc, initialColor, color)
        return image

    def floodFillHelper(self, image, row, col, initialColor, newColor):
        if row < 0 or row >= len(image) or col < 0 or col >= len(image[0]):
            return

        cellColor = image[row][col]
        if cellColor != initialColor:
            return

        image[row][col] = newColor
        self.floodFillHelper(image, row+1, col, initialColor, newColor)
        self.floodFillHelper(image, row-1, col, initialColor, newColor)
        self.floodFillHelper(image, row, col+1, initialColor, newColor)
        self.floodFillHelper(image, row, col-1, initialColor, newColor)
