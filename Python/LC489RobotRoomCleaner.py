class Solution:
    
    """
    This is a DFS problem, but we dont have a "board" or space. We have to create one and memorize the visited one  in code.
    The key is how to let robot do "backtracking":
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
    but before that, when a robot reaches a new cell, it needs to be aware of its facing, since it is used to compute its current coordinate and all its neighbor's coordinate, so that we can determine if a neighbr has been visited or not.
    
    """
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        
        def dfs(robot, x, y, seen, facing):
            nonlocal directions
            robot.clean()
            seen.add((x, y))
            for i in range(4):
                new_facing = (facing + i) % 4
                x1, y1 = x + directions[new_facing][0], y + directions[new_facing][1]
                if (x1, y1) not in seen and robot.move():
                    dfs(robot, x1, y1, seen, new_facing)
                robot.turnRight()
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
        dfs(robot, 0, 0, set(), 0)
        
                
        
        
        
        
        
        
