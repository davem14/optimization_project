from math import exp

from numpy.random import rand

from problems import Problem
from solvers import Solver


class SimulatedAnnealing(Solver):
    def __init__(self, problem: Problem, init_state: tuple, cooling_factor: float = 0.97, batch_size: int = 1):
        super().__init__(problem, init_state, batch_size)
        self.iteration = 1
        self.temp = 1
        self.cooling_factor = cooling_factor

    def is_preferred_state(self, state, diff: float) -> bool:
        return diff > 0 or rand() < exp(diff / self.temp)

    def state_changed(self):
        self.temp *= self.cooling_factor
