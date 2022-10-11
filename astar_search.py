from SearchSolution import SearchSolution
from heapq import heappush, heappop


class AstarNode:
    # each search node except the root has a parent node
    # and all search nodes wrap a state object

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

    # comparison operator,
    # needed for heappush and heappop to work with AstarNodes:
    def __lt__(self, other):
        return self.priority() < other.priority()


# take the current node, and follow its parents back
#  as far as possible. Grab the states from the nodes,
#  and reverse the resulting list of states.
def backchain(node):
    result = []
    current = node
    while current:
        result.append(current.state)
        current = current.parent

    result.reverse()
    return result


def astar_search(search_problem, heuristic_fn):
    start_node = AstarNode(search_problem.start_state, heuristic_fn(search_problem.start_state))
    pqueue = []
    heappush(pqueue, start_node)

    solution = SearchSolution(search_problem, "Astar with heuristic " + heuristic_fn.__name__)

    visited_cost = {start_node.state: 0}

    while pqueue:
        node = heappop(pqueue)

        if search_problem.goal_test(node.state):
            solution.path = backchain(node)
            solution.cost = node.cost
            return solution

        children = search_problem.get_successors(node.state)
        for child in children:
            solution.nodes_visited += 1
            transition_cost = search_problem.transition_cost(node.state, child)
            cost = node.cost + transition_cost

            if child not in visited_cost or visited_cost[child] > cost:
                visited_cost[child] = cost
                heuristic = heuristic_fn(child)
                child_node = AstarNode(child, heuristic, node, transition_cost)
                heappush(pqueue, child_node)

    return solution
