import random

from problems import NQueens
from problems import TravelingSalesman
from solvers import HillClimbing, SimulatedAnnealing

if __name__ == '__main__':
    pr = TravelingSalesman()
    # init = ((1,9), (17,10), (3,7), (20,12), (5,10), (7,11), (5,3), (3,2), (0,4), (6,9), (27,12), (15,23), (22, 17), (1, 23), (11, 10), (21,2))
    # init = ((1,3), (2,5), (2,15), (2,1), (3,3), (7,15), (2,-7), (7,-7))
    init = tuple(set((random.randint(0, 100), random.randint(0, 100)) for _ in range(20)))

    n = 5
    # pr = NQueens(n)
    # init = tuple(i for i in range(n))

    s = SimulatedAnnealing(pr, init, cooling_factor=.9)
    solution = s()
    print(pr.evaluate(solution))
    pr.show(solution)
    input("press enter to exit")
