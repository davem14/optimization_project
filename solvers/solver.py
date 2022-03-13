from abc import ABC

import matplotlib.pyplot as plt

from problems import Problem


class Solver(ABC):
    def __init__(self, problem: Problem, init_state: tuple):
        self._problem = problem
        self._state = init_state
        self._values = [problem.evaluate(init_state)]
        self._running = True
        plt.show()

    def __call__(self):
        while self._running:
            changed = False
            neighbors = self._problem.neighbors(self._state)
            for neighbor in neighbors:
                neighbor_val = self._problem.evaluate(neighbor)
                if self.is_preferred_state(neighbor, self._values[-1] - neighbor_val):
                    self._values.append(neighbor_val)
                    self._state = neighbor
                    self.state_changed()
                    changed = True
                    print(self._state, neighbor_val)
                    self._problem.show(self._state)
                    break
            if not changed:
                return self._state

    def is_preferred_state(self, state, val) -> bool:
        raise NotImplementedError

    def state_changed(self):
        raise NotImplementedError
