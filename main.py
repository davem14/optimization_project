import random
import time
from math import inf

from problems import NQueens
from problems import TravelingSalesman
from solvers import HillClimbing, SimulatedAnnealing, TabuSearch

if __name__ == '__main__':
    pr = TravelingSalesman()
    # init = ((1,9), (17,10), (3,7), (20,12), (5,10), (7,11), (5,3), (3,2), (0,4), (6,9), (27,12), (15,23), (22, 17), (1, 23), (11, 10), (21,2))
    # init = ((1,3), (2,5), (2,15), (2,1), (3,3), (7,15), (2,-7), (7,-7))
    # init = ((70, 81), (66, 79), (99, 84), (82, 95), (54, 88), (14, 81), (7, 76), (23, 74), (35, 66), (59, 58), (75, 19), (30, 9), (16, 43), (24, 46), (36, 42), (44, 46), (52, 93), (25, 36), (42, 55), (78, 85))
    init = tuple(set((random.randint(0, 100), random.randint(0, 100)) for _ in range(40)))

    # n = 5
    # pr = NQueens(n)
    # init = tuple(i for i in range(n))

    for s in [
        HillClimbing(pr, init, batch_size=inf),
        SimulatedAnnealing(pr, init, cooling_factor=.9),
        TabuSearch(pr, init, max_iterations=len(init)**2, tabu_list_size=len(init)*10)
    ]:
        t = time.time()
        solution = s()
        print(pr.evaluate(solution), time.time() - t)
        pr.show(solution)
        input("press enter to exit")
