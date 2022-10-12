# Author: Xiaoxuan
# Date: 10/8/2022
# Purpose: a description of the search problem.
# Multiple robots need to get to their goal locations.
# They take turns to move.
# They can't run into walls or each other.
from Maze import Maze
from time import sleep


class MazeworldProblem:
    # state: [turn, x1, y1, x2, y2, ..., xn, yn]
    def __init__(self, maze, goal_locations):
        self.maze = maze
        self.start_state = [0] + self.maze.robotloc
        self.goal_locations = goal_locations
        self.num_robots = len(self.maze.robotloc) // 2

    def get_successors(self, state):
        successors = []
        turn = state[0]
        offset = 2*turn + 1
        x, y = state[offset], state[offset+1]

        # update the turn
        turn += 1
        turn = turn % self.num_robots

        # if the robot doesn't move
        successors.append([turn]+state[1:])

        # if the robot moves in any of the four directions
        self.maze.robotloc = state[1:]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for direction in directions:
            nx = x + direction[0]
            ny = y + direction[1]
            if self.legality_test(nx, ny):
                successors.append([turn]+state[1:offset]+[nx, ny]+state[offset+2:])

        return successors

    # make sure a location is safe
    def legality_test(self, x, y):
        return self.maze.is_floor(x, y) and not self.maze.has_robot(x, y)

    # test whether we have reached the goal
    def goal_test(self, state):
        return state[1:] == self.goal_locations

    # if the robot moves, transition cost is 1
    # if the robot doesn't move, transition cost is 0
    def transition_cost(self, start_state, end_state):
        if start_state[1:] == end_state[1:]:
            return 0
        return 1

    # how far away a state is from the goal state
    def manhattan_heuristic(self, state):
        heuristic = 0
        for i in range(len(state)-1):
            heuristic += abs(state[i+1]-self.goal_locations[i])
        return heuristic

    # given a sequence of states (including robot turn), modify the maze and print it out.
    def animate_path(self, path):
        # reset the robot locations in the maze
        self.maze.robotloc = self.start_state[1:]

        for state in path:
            self.maze.robotloc = state[1:]
            sleep(1)
            print(str(self.maze))

    def __str__(self):
        string = "Mazeworld problem:\n" + str(self.maze)
        return string


if __name__ == "__main__":
    mp3 = MazeworldProblem(Maze("maze3.maz"), [1, 4, 1, 3, 1, 2])
    print(mp3.get_successors(mp3.start_state))
    print(mp3.get_successors([0, 1, 0, 1, 2, 2, 1]))
