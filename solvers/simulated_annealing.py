from math import exp

from numpy.random import rand, randn

from problems import Problem
from solvers import Solver


class SimulatedAnnealing(Solver):
    def __init__(self, problem: Problem, init_state: tuple):
        super().__init__(problem, init_state)
        self.iteration = 1

    def is_preferred_state(self, state, diff: float) -> bool:
        temp = 1 / float(self.iteration)
        return diff > 0 or rand() < exp(diff / temp)

    def state_changed(self):
        self.iteration += 1



    # simulated annealing algorithm
    # https://machinelearningmastery.com/simulated-annealing-from-scratch-in-python/
    @staticmethod
    def simulated_annealing(objective, bounds, n_iterations, step_size, temp):
        # generate an initial point
        best = bounds[:, 0] + rand(len(bounds)) * (bounds[:, 1] - bounds[:, 0])
        # evaluate the initial point
        best_eval = objective(best)
        # current working solution
        curr, curr_eval = best, best_eval
        # run the algorithm
        for i in range(n_iterations):
            # take a step
            candidate = curr + randn(len(bounds)) * step_size
            # evaluate candidate point
            candidate_eval = objective(candidate)
            # check for new best solution
            if candidate_eval < best_eval:
                # store new best point
                best, best_eval = candidate, candidate_eval
                # report progress
                print('>%d f(%s) = %.5f' % (i, best, best_eval))
            # difference between candidate and current point evaluation
            diff = candidate_eval - curr_eval
            # calculate temperature for current epoch
            t = temp / float(i + 1)
            # calculate metropolis acceptance criterion
            metropolis = exp(-diff / t)
            # check if we should keep the new point
            if diff > 0 or rand() < metropolis:
                # store the new current point
                curr, curr_eval = candidate, candidate_eval
        return [best, best_eval]