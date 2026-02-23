import math
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
    # TODO: Add your code here
    x1, y1 = state
    x2, y2 = problem.goal
    
    return abs(x1 - x2) + abs(y1 - y2)    


def euclideanHeuristic(state, problem):
    """
    The Euclidean distance heuristic.
    """
    # TODO: Add your code here
    x1, y1 = state
    
    x2, y2 = problem.goal

    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


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
    """
    Estuvimos bastante tiempo pensando en este heuriística, pero tras revisar diferentes fuentes no supimos como empezarla nisiquiera con las pistas dadas,
    por lo que le solicitamos ayuda a ChatGPT para que nos diera una idea de como empezar a implementarla, y luego de eso pudimos terminarla nosotros mismos.
    Prompt: "Chat, estamos un poco perdidos y no sabemos como empezar a enfrentar esta heurística, podrías ayudarnos para poder aclararnos dudas y que luego
    podamos terminarla?"

    Nos arrojó lo siguiente:
    
    def survivorHeuristic(state: Tuple[Tuple, Any], problem: MultiSurvivorProblem):

    # 1️ Separar el estado
    position, survivors_grid = state

    # 2️ Obtener lista de sobrevivientes restantes
    survivors = survivors_grid.asList()

    # 3️ Caso base: si no quedan sobrevivientes
    if len(survivors) == 0:
        return 0

    # 4️ Distancia Manhattan al sobreviviente más cercano
    distances = []
    for s in survivors:
        dist = abs(position[0] - s[0]) + abs(position[1] - s[1])
        distances.append(dist)

    nearest = min(distances)

    # 5️ (Aquí luego agregan algo más...)

    return nearest


    Luego, fuimos construyendo de a poco pero decidimos que seria buena idea que nos guiara con una estructura de como se debia ver, cuestión de que nuestra tarea sea realizar la totalidad de la lógica
    Prompt: "Listo, hemos ido avanzando pero creemos que sería de gran ayuda que nos mandes la estructura general de como se debe ver la función, obvio sin la lógica, para que nosotros podamos terminarla,
    pero esto servirá de guía de que lo que estamos haciendo esta bien"

    Recibimos esto:

    def survivorHeuristic(state: Tuple[Tuple, Any], problem: MultiSurvivorProblem):

    # ------------------------------------
    # 1️⃣ Desempaquetar el estado
    # ------------------------------------
    position, survivors_grid = state

    # ------------------------------------
    # 2️⃣ Obtener sobrevivientes restantes
    # ------------------------------------
    survivors = survivors_grid.asList()

    # ------------------------------------
    # 3️⃣ Caso base: no quedan sobrevivientes
    # ------------------------------------
    if len(survivors) == 0:
        return 0

    # ------------------------------------
    # 4️⃣ Distancia al sobreviviente más cercano
    # ------------------------------------
    nearest = 0
    # AQUÍ: calcular distancia mínima desde position a survivors

    # ------------------------------------
    # 5️⃣ Costo de conectar sobrevivientes (MST)
    # ------------------------------------
    mst_cost = 0
    # AQUÍ: calcular MST entre survivors usando Manhattan

    # ------------------------------------
    # 6️⃣ Retornar suma (lower bound total)
    # ------------------------------------
    return nearest + mst_cost


    Ya con base a esto, supimos como armar la heurística en su totalidad, viendose a continuación
    """

    """
    Admisible: nearest survivor distance + MST(survivors) with Manhattan weights.
    Uses caching in problem.heuristicInfo to speed up repeated calls.
    """
    position, survivors_grid = state

   
    survivors = survivors_grid.asList()
    if len(survivors) == 0:
        return 0

    
    info = problem.heuristicInfo

  
    if "pairDist" not in info:
        info["pairDist"] = {}
    pairDist = info["pairDist"]

    if "mstCost" not in info:
        info["mstCost"] = {}
    mstCache = info["mstCost"]

    def manhattan(a, b):
      
        key = (a, b) if a <= b else (b, a)
        if key in pairDist:
            return pairDist[key]
        d = abs(a[0] - b[0]) + abs(a[1] - b[1])
        pairDist[key] = d
        return d

   
    nearest = min(manhattan(position, s) for s in survivors)

    
    surv_set = frozenset(survivors)
    if surv_set in mstCache:
        mst_cost = mstCache[surv_set]
    else:
        nodes = list(surv_set)
        if len(nodes) <= 1:
            mst_cost = 0
        else:
            in_tree = set()
            start = nodes[0]
            in_tree.add(start)

            
            best = {}
            for v in nodes[1:]:
                best[v] = manhattan(start, v)

            mst_cost = 0
            while len(in_tree) < len(nodes):
            
                v_min = min(best, key=best.get)
                w = best.pop(v_min)
                mst_cost += w
                in_tree.add(v_min)

              
                for v in list(best.keys()):
                    cand = manhattan(v_min, v)
                    if cand < best[v]:
                        best[v] = cand

        mstCache[surv_set] = mst_cost

    return nearest + mst_cost
