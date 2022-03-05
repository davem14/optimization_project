from problems.n_queens import NQueens
from problems.traveling_salesman import TravelingSalesman
from solvers.solver import Solver

if __name__ == '__main__':
    # pr = TravelingSalesman()
    # cities = ((1,9), (3,7), (5,10), (7,11), (5,3), (3,2), (0,4), (6,9), (27,12), (15,23), (43, 1), (22, 17), (1, 23), (11, 10), (21,2))
    # s = Solver(pr, cities)
    # solution = s()
    # print(pr.evaluate(solution))

    n = 7
    pr = NQueens(n)
    init = tuple(i for i in range(n))
    s = Solver(pr, init)
    solution = s()
    print(pr.evaluate(solution))
    pr.show(solution)
