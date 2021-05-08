class Solution(object):

    def dfs(self, image, sr, sc, newColor, origin):
        directs = [[0,-1], [0,1], [-1,0], [1,0]]
        m = len(image)
        n = len(image[0])
        for direct in directs:
            nx = sr + direct[0]
            ny = sc + direct[1]
            if nx<0 or nx>=m or ny<0 or ny>=n: continue
            if image[nx][ny] == origin:
                image[nx][ny] = newColor
                self.dfs(image, nx, ny, newColor, origin)

    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        m = len(image)
        if m <= 0: return image
        n = len(image[0])
        if sr >= m or sc >= n: return image
        origin = image[sr][sc]
        if origin == newColor: return image
        image[sr][sc] = newColor
        self.dfs(image, sr, sc, newColor, origin)
        return image
s = Solution()
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1; sc = 1; newColor = 2
print(s.floodFill(image, sr, sc, newColor))