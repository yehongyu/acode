class Solution():
    class Robot():
        def move(self):
            print('move')
            return True
        def trunLeft(self):
            print('trun left')
            return True
        def trunRight(self):
            print('trun right')
            return True
        def clean(self):
            print('clean')
            return True

    def dfs(self, robot, visited, x, y, dir):
        robot.clean()
        visited.add(x + '#' + y)
        directs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        for i in range(4):
            cur = (dir + i) % 4;
            nx = x + directs[cur][0]
            ny = y + directs[cur][1]
            if (nx + '#' + ny) in visited and robot.move():
                self.dfs(robot, visited, nx, ny, cur)
                robot.turnRight()
                robot.turnRight()
                robot.move()
                robot.turnLeft()
                robot.turnLeft()
            robot.turnRight()

    def cleanRoom(self, robot):
        visited = set()
        self.dfs(robot, visited, 0, 0, 0)

