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
    # TODO: Add your code here
    utils.raiseNotDefined()


def breadthFirstSearch(problem: SearchProblem):
    """
    Search the shallowest nodes in the search tree first.
    """
    # TODO: Add your code here
    utils.raiseNotDefined()


def uniformCostSearch(problem: SearchProblem):
    """
    Search the node of least total cost first.
    """

    """ VERSION 0 UCS, RESOLVÍA LOS PROBLEMAS PERO NO DE UNA MANERA MUY EFICIENTE

    def uniformCostSearch(problem):
        Cola= utils.PriorityQueue()

        start = problem.getStartState()
        Cola.push((start, []), 0)  

        visited = set()

        while not Cola.isEmpty():
            state, actions = Cola.pop()

            if state in visited:
                continue
            visited.add(state)

            if problem.isGoalState(state):
                return actions

            successors = problem.getSuccessors(state)

            for successor in successors:
                succ = successor[0]
                action = successor[1]

                newActions = actions.copy()
                newActions.append(action)

                cost = problem.getCostOfActions(newActions)

                Cola.push((succ, newActions), cost)

        return []

        PROMPT USADO PARA LA OPTIMIZACIÓN: "Hola chat, quisiera que me ayudaras a optimizar el código que ya tengo, como puedo hacerlo? sin afectar la lógica de otros códigos,
                                            unicamente moviendo lo que respecte a UCS"
        LA CORRECCIÓN DADA POR GPT FUE LA QUE SE EVIDENCIA EN EL CÓDIGO DEFINITIVO (EN LOS COMENTARIOS DEL CÓDIGO EXPLICO LAS OPTIMIZACIONES REALIZADAS)

        
        """
    Cola = utils.PriorityQueue()

    start = problem.getStartState()

    # (estado, acciones, costo_acumulado)
    Cola.push((start, [], 0), 0)

    bestCost = {start: 0}

    while not Cola.isEmpty():
        state, actions, cost = Cola.pop()

        # Si este camino ya no es el mejor conocido, lo ignoramos
        if cost > bestCost.get(state, float("inf")):
            continue

        if problem.isGoalState(state):
            return actions

        successors = problem.getSuccessors(state)

        for successor in successors:
            succ = successor[0]
            action = successor[1]
            stepCost = successor[2]

            newCost = cost + stepCost

            # Solo lo meto si mejora el mejor costo conocido hacia succ
            if newCost < bestCost.get(succ, float("inf")):
                bestCost[succ] = newCost

                newActions = actions.copy()
                newActions.append(action)

                Cola.push((succ, newActions, newCost), newCost)

    return []

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """
    CODIGO VERSION 0, NO ME CORRIA YA QUE DABA EL SIGUIENTE ERROR ValueError: too many values to unpack (expected 2)
    def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
        cola = utils.PriorityQueue()
        start = problem.getStartState()

        cola.push((start, [], 0), heuristic(start, problem))

        while not cola.isEmpty():
            state, actions, g = cola.pop()

            if problem.isGoalState(state):
                return actions

            for succ, action in problem.getSuccessors(state): 
                newG = g + 1
                f = newG + heuristic(succ, problem)
                cola.push((succ, actions + [action], newG), f)

        return []
        
        El error fue corregido de manera manual mas sin embargo utilicé la IA para ayudarme a optimizar el resultado obtenido,
         
          Prompt: "Listo, ya pude corregir el error y está dando unos resultados que a pesar de que resuelve la búsqueda, siento que se puede hacer de manera más eficiente, por favor ayudame a optimizarlo"
            el código final es el siguiente:
        """

    Cola = utils.PriorityQueue()

    start = problem.getStartState()

    Cola.push((start, [], 0), heuristic(start, problem))

    bestCost = {start: 0}

    while not Cola.isEmpty():
        state, actions, g = Cola.pop()
        if g != bestCost.get(state, float("inf")):
            continue

        if problem.isGoalState(state):
            return actions

        for succ, action, stepCost in problem.getSuccessors(state):
            newG = g + stepCost

            if newG < bestCost.get(succ, float("inf")):
                bestCost[succ] = newG

                newActions = actions + [action]
                f = newG + heuristic(succ, problem)

                Cola.push((succ, newActions, newG), f)

    return []
    
    
        


# Abbreviations (you can use them for the -f option in main.py)
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
