from abc import ABC

import matplotlib.pyplot as plt

from problems import Problem


class Solver(ABC):
    def __init__(self, problem: Problem, init_state: tuple, batch_size: int = 1):
        self._problem = problem
        self._batch_size = batch_size
        self._state = init_state
        self._values = [problem.evaluate(init_state)]
        self._running = True
        plt.show()

    def __call__(self):
        while self._running:
            changed = False
            neighbors = self._problem.neighbors(self._state)
            for neighbors_batch in self.split_to_batches(neighbors):
                neighbor = self.choose_best_from_batch(neighbors_batch)
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

    def split_to_batches(self, neighbors):
        batch = []
        for i, neighbor in enumerate(neighbors, 1):
            batch.append(neighbor)
            if i % self._batch_size == 0:
                yield batch
                batch = []
        if batch:
            yield batch

    def choose_best_from_batch(self, neighbors):
        return sorted(neighbors, key=lambda n: self._problem.evaluate(n))[0]

    def is_preferred_state(self, state, val) -> bool:
        raise NotImplementedError

    def state_changed(self):
        raise NotImplementedError
