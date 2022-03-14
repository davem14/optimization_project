import random
import time
from math import inf

from problems import NQueens
from problems import TravelingSalesman
from solvers import HillClimbing, SimulatedAnnealing, TabuSearch

if __name__ == '__main__':
    # pr = TravelingSalesman()
    # init = tuple(set((random.randint(0, 100), random.randint(0, 100)) for _ in range(40)))

    n = 3
    pr = NQueens(n)
    init = tuple(i for i in range(n))

    for solver in [
        HillClimbing(pr, init, max_iterations=10000, batch_size=inf),
        SimulatedAnnealing(pr, init, max_iterations=100000, cooling_factor=.9),
        TabuSearch(pr, init, max_iterations=100000, batch_size=inf)
    ]:
        t = time.time()
        solution = solver()
        print(solver.best_val, time.time() - t, "iters =", solver.iteration)
        pr.show(solver.best_state)
        input("press enter to exit")
