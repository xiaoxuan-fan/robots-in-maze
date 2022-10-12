# Author: Xiaoxuan
# Date: 10/7/2022
# Purpose: Implement A* search
from SearchSolution import SearchSolution
from heapq import heappush, heappop


# wrap state in a node
class AstarNode:

    def __init__(self, state, heuristic, parent=None, transition_cost=0):
        self.state = state
        self.heuristic = heuristic
        self.parent = parent
        if parent is None:
            self.cost = 0
        else:
            self.cost = parent.cost + transition_cost

    def priority(self):
        return self.cost + self.heuristic

    # comparison operator needed for heapq
    def __lt__(self, other):
        return self.priority() < other.priority()


# given a node, find its way back to the start node
# return a list of states
def backchain(node):
    result = []
    current = node
    while current:
        result.append(current.state)
        current = current.parent

    result.reverse()
    return result


# A* search
def astar_search(search_problem, heuristic_fn):
    solution = SearchSolution(search_problem, "Astar with heuristic " + heuristic_fn.__name__)
    start_node = AstarNode(search_problem.start_state, heuristic_fn(search_problem.start_state))
    visited_cost = {}
    pqueue = []

    heappush(pqueue, start_node)
    visited_cost[str(start_node.state)] = 0
    while pqueue:
        node = heappop(pqueue)
        state = node.state

        if search_problem.goal_test(state):
            solution.path = backchain(node)
            solution.cost = node.cost
            return solution

        children = search_problem.get_successors(state)
        for child in children:
            solution.nodes_visited += 1
            transition_cost = search_problem.transition_cost(state, child)
            cost = node.cost + transition_cost

            if str(child) not in visited_cost or visited_cost[str(child)] > cost:
                visited_cost[str(child)] = cost
                heuristic = heuristic_fn(child)
                child_node = AstarNode(child, heuristic, node, transition_cost)
                heappush(pqueue, child_node)

    return solution
