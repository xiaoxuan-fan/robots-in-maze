from MazeworldProblem import MazeworldProblem
from Maze import Maze
from astar_search import astar_search


# uniform cost search (heuristic=0)
def null_heuristic(state):
    return 0


# Create a few test problems:
mp2 = MazeworldProblem(Maze('maze2.maz'), [0, 1])
mp3 = MazeworldProblem(Maze('maze3.maz'), [1, 4, 1, 3, 1, 2])

print(astar_search(mp2, null_heuristic))
print(astar_search(mp2, mp2.manhattan_heuristic))

print(astar_search(mp3, null_heuristic))
solution = astar_search(mp3, mp3.manhattan_heuristic)
print(solution)
mp3.animate_path(solution.path)
