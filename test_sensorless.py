from SensorlessProblem import SensorlessProblem
from Maze import Maze
from astar_search import astar_search


# uniform cost search (heuristic=0)
def null_heuristic(state):
    return 0


# Create a few test problems:
sp1 = SensorlessProblem(Maze('maze1.maz'))
print(astar_search(sp1, null_heuristic))
solution = astar_search(sp1, sp1.naive_heuristic)
print(solution)
# sp1.animate_path(solution.path)

sp3 = SensorlessProblem(Maze('maze3.maz'))
print(astar_search(sp3, null_heuristic))
print(astar_search(sp3, sp3.naive_heuristic))

sp5 = SensorlessProblem(Maze('maze5.maz'))
print(astar_search(sp5, null_heuristic))
print(astar_search(sp5, sp5.naive_heuristic))

sp4 = SensorlessProblem(Maze('maze4.maz'))
print(astar_search(sp4, null_heuristic))
print(astar_search(sp4, sp4.naive_heuristic))
