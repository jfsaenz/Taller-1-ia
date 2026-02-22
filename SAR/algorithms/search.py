from algorithms.problems import SearchProblem
import algorithms.utils as utils
from world.game import Directions
from algorithms.heuristics import nullHeuristic


def tinyHouseSearch(problem: SearchProblem):
    """
    Returns a sequence of moves that solves tinyHouse. For any other building, the
    sequence of moves will be incorrect, so only use this for tinyHouse.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    # Initialize the stack with the start state and empty path
    start_state = problem.getStartState()
    stack = [(start_state, [])]  # (state, path)
    visited = set([start_state])
    
    while stack:
        current_state, path = stack.pop()
        
        if problem.isGoalState(current_state):
            return path
        
        # Get successors
        for successor, action, cost in problem.getSuccessors(current_state):
            if successor not in visited:
                visited.add(successor)
                new_path = path + [action]
                stack.append((successor, new_path))
    
    # If no solution found
    return []


def breadthFirstSearch(problem: SearchProblem):
    """
    Search the shallowest nodes in the search tree first.
    """
    # Código Original Hecho a mano, sin IA:
    """
    frontier = utils.Queue()
    start = problem.getStartState()

    frontier.push((start, []))
    visited = set([start])

    while not frontier.isEmpty():
        state, path = frontier.pop()

        if problem.isGoalState(state):
            return path

        for succ, action, stepCost in problem.getSuccessors(state):
            if succ not in visited:
                visited.add(succ)
                frontier.push((succ, path + [action]))

    return []
    """
    #PROMPT: Revisa la carpeta que tiene todo el código, con eso, revisa el código que hice para BFS, 
    #Corrigelo en caso de ser necesario para que cumpla con lo que me piden en el documento.
    #El código que hice fue este: (Código Original Hecho a mano, sin IA)
    
    #Código corregido por IA (ChatGPT 5.2 versión Plus):
    # TODO: Add your code here
    start = problem.getStartState()
    if problem.isGoalState(start):
        return []

    frontier = utils.Queue()
    frontier.push(start)

    visited = set([start])
    parent = {}  

    while not frontier.isEmpty():
        state = frontier.pop()

        if problem.isGoalState(state):
            actions = []
            cur = state
            while cur != start:
                prev, act = parent[cur]
                actions.append(act)
                cur = prev
            actions.reverse()
            return actions

        for succ, action, stepCost in problem.getSuccessors(state):
            if succ not in visited:
                visited.add(succ)
                parent[succ] = (state, action)
                frontier.push(succ)

    return []


def uniformCostSearch(problem: SearchProblem):
    """
    Search the node of least total cost first.
    """

    # TODO: Add your code here
    utils.raiseNotDefined()


def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    # TODO: Add your code here
    utils.raiseNotDefined()


# Abbreviations (you can use them for the -f option in main.py)
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
