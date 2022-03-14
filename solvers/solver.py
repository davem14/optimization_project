from abc import ABC
from math import inf

import matplotlib.pyplot as plt

from problems import Problem


class Solver(ABC):
    def __init__(self, problem: Problem, init_state: tuple, batch_size=1, max_iterations=inf):
        self.problem = problem
        self.batch_size = batch_size
        self.state = init_state
        self.best_state = init_state
        self.best_val = problem.evaluate(init_state)
        self.values = [problem.evaluate(init_state)]
        self.max_iterations = max_iterations
        self.iteration = 0
        plt.show()

    def __call__(self):
        while self.running():
            self.iteration += 1
            changed = False
            neighbors = self.problem.neighbors(self.state)
            for neighbors_batch in self.split_to_batches(neighbors):
                neighbor = self.choose_best_from_batch(neighbors_batch)
                if not neighbor:
                    continue
                neighbor_val = self.problem.evaluate(neighbor)
                if neighbor_val < self.best_val:
                    self.best_val = neighbor_val
                    self.best_state = neighbor
                    if self.best_val == self.problem.optimal_val:
                        return
                if self.is_preferred_state(neighbor, self.values[-1] - neighbor_val):
                    self.values.append(neighbor_val)
                    self.state = neighbor
                    self.state_changed()
                    changed = True
                    # print(self.iteration, neighbor_val, self.best_val)
                    # self.problem.show(self.state)
                    break
            if not changed:
                return

    def running(self):
        return self.iteration < self.max_iterations

    def split_to_batches(self, neighbors):
        batch = []
        for i, neighbor in enumerate(neighbors, 1):
            batch.append(neighbor)
            if i % self.batch_size == 0:
                yield batch
                batch = []
        if batch:
            yield batch

    def choose_best_from_batch(self, neighbors):
        return sorted(neighbors, key=lambda n: self.problem.evaluate(n))[0]

    def is_preferred_state(self, state, val) -> bool:
        return True

    def state_changed(self):
        raise NotImplementedError
