# Author: Xiaoxuan
# Date: 10/10/2022
# Purpose: a description of the search problem.
# One blind robot that doesn't know where it is,
# but has the map and knows the direction it's going in.
from Maze import Maze
from time import sleep


class SensorlessProblem:
    # state: set of possible robot locations
    def __init__(self, maze):
        self.maze = maze
        self.start_state = set()
        for x in range(self.maze.width):
            for y in range(self.maze.height):
                if self.legality_test(x, y):
                    self.start_state.add((x, y))

    def get_successors(self, state):
        successors = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for direction in directions:
            new_state = set()
            for loc in state:
                nx = loc[0]+direction[0]
                ny = loc[1]+direction[1]
                if self.legality_test(nx, ny):
                    new_state.add((nx, ny))
                else:
                    new_state.add(loc)
            successors.append(new_state)

        return successors

    def legality_test(self, x, y):
        return self.maze.is_floor(x, y)

    def goal_test(self, state):
        return len(state) == 1

    def transition_cost(self, start_state, end_state):
        return 1

    def naive_heuristic(self, state):
        return len(state)

    def update_locations(self, state):
        locations = []
        for loc in state:
            locations.append(loc[0])
            locations.append(loc[1])
        self.maze.robotloc = locations

    # given a sequence of states, modify the maze and print it out.
    def animate_path(self, path):
        # reset the robot locations in the maze
        self.update_locations(self.start_state)

        for state in path:
            self.update_locations(state)
            sleep(1)
            print(str(self.maze))

    def __str__(self):
        string = "Blind robot problem:\n" + str(self.maze)
        return string


if __name__ == "__main__":
    sp1 = SensorlessProblem(Maze('maze1.maz'))
    print(sp1.start_state)
    print(sp1.get_successors(sp1.start_state))
