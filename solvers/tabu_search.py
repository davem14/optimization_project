from collections import deque
from math import inf

from solvers import Solver


class TabuSearch(Solver):
    def __init__(self, problem, init_state, max_iterations: int, tabu_list_size: int, batch_size=inf):
        super().__init__(problem, init_state, batch_size, max_iterations=max_iterations)
        self._tabu_list = deque([init_state], tabu_list_size)

    def choose_best_from_batch(self, neighbors):
        legal_neighbors = [neighbor for neighbor in neighbors if neighbor not in self._tabu_list]
        if not legal_neighbors:
            return None
        return super().choose_best_from_batch(legal_neighbors)

    def is_preferred_state(self, state, val) -> bool:
        return bool(state)

    def state_changed(self):
        self._tabu_list.append(self._state)
