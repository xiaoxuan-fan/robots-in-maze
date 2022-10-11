from Maze import Maze
from time import sleep


class MazeworldProblem:

    def __init__(self, maze, goal_locations):
        self.maze = maze
        self.goal_locations = goal_locations
        self.start_state = [0] + self.maze.robotloc
        self.num_robots = len(self.maze.robotloc) / 2

    def __str__(self):
        string = "Mazeworld problem: "
        return string

    def get_successors(self, state):
        successors = []
        turn = state[0]
        self.maze.robotloc = state[1:]
        offset = 2*turn + 1
        x, y = state[offset], state[offset+1]

        # update the turn
        turn += 1
        turn = turn % self.num_robots

        print(state)
        # if the robot doesn't move
        successors.append([turn]+state[1:])

        # if the robot moves in any of the four directions
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for direction in directions:
            nx = x + direction[0]
            ny = y + direction[1]
            if self.legality_test(nx, ny):
                successors.append([turn]+state[1:offset]+[nx, ny]+state[offset+2:])

        return successors

    def legality_test(self, x, y):
        return self.maze.is_floor(x, y) and not self.maze.has_robot(x, y)

    def goal_test(self, state):
        return state[1:] == self.goal_locations

    def transition_cost(self, start_state, end_state):
        if start_state[1:] == end_state[1:]:
            return 1
        return 0

    def manhattan_heuristic(self, state):
        heuristic = 0
        for i in range(1, len(state)):
            heuristic += abs(state[i]-self.goal_locations[i])
        return heuristic

    # given a sequence of states (including robot turn), modify the maze and print it out.
    def animate_path(self, path):
        # reset the robot locations in the maze
        self.maze.robotloc = self.start_state[1:]

        for state in path:
            print(str(self))
            self.maze.robotloc = state[1:]
            sleep(1)
            print(str(self.maze))


if __name__ == "__main__":
    test_maze3 = Maze("maze3.maz")
    test_mp = MazeworldProblem(test_maze3, [1, 4, 1, 3, 1, 2])

    print(test_mp.get_successors([0, 1, 0, 1, 2, 2, 1]))
