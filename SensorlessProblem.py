# Author: Xiaoxuan
# Date: 10/9/2022
# Purpose: a description of the search problem.
# One robot
# They take turns to move.
# They can't run into walls or each other.
from Maze import Maze
from time import sleep


class SensorlessProblem:

    ## You write the good stuff here:

    def __str__(self):
        string = "Blind robot problem: "
        return string

        # given a sequence of states (including robot turn), modify the maze and print it out.
        #  (Be careful, this does modify the maze!)

    def animate_path(self, path):
        # reset the robot locations in the maze
        self.maze.robotloc = tuple(self.start_state)

        for state in path:
            print(str(self))
            self.maze.robotloc = tuple(state)
            sleep(1)

            print(str(self.maze))


## A bit of test code

if __name__ == "__main__":
    test_maze3 = Maze("maze3.maz")
    test_problem = SensorlessProblem(test_maze3)
