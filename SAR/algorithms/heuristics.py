from typing import Any, Tuple
from algorithms import utils
from algorithms.problems import MultiSurvivorProblem


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def manhattanHeuristic(state, problem):
    """
    The Manhattan distance heuristic.

    For SimpleSurvivorProblem: calculates |dx| + |dy| between current position and goal
    For MultiSurvivorProblem: calculates distance to nearest remaining survivor
    """
    # Handle different state formats
    if isinstance(state, tuple) and len(state) == 2 and isinstance(state[0], tuple):
        # MultiSurvivorProblem: state = (position, survivors_grid)
        position = state[0]
        survivors_grid = state[1]   

        # Find nearest survivor
        min_distance = float('inf')
        for x in range(survivors_grid.width):
            for y in range(survivors_grid.height):
                if survivors_grid[x][y]:  # Survivor present
                    distance = abs(position[0] - x) + abs(position[1] - y)
                    min_distance = min(min_distance, distance)

        return min_distance if min_distance != float('inf') else 0

    else:
        # SimpleSurvivorProblem: state = (x, y) position
        current_x, current_y = state
        goal_x, goal_y = problem.goal

        # Manhattan distance: |dx| + |dy|
        return abs(current_x - goal_x) + abs(current_y - goal_y)


def euclideanHeuristic(state, problem):
    """
    The Euclidean distance heuristic.
    """
    # TODO: Add your code here
    utils.raiseNotDefined()


def survivorHeuristic(state: Tuple[Tuple, Any], problem: MultiSurvivorProblem):
    """
    Your heuristic for the MultiSurvivorProblem.

    state: (position, survivors_grid)
    problem: MultiSurvivorProblem instance

    This must be admissible and preferably consistent.

    Hints:
    - Use problem.heuristicInfo to cache expensive computations
    - Go with some simple heuristics first, then build up to more complex ones
    - Consider: distance to nearest survivor + MST of remaining survivors
    - Balance heuristic strength vs. computation time (do experiments!)
    """
    # TODO: Add your code here
    utils.raiseNotDefined()
