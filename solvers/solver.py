from random import shuffle
from time import sleep

from problems.n_queens import NQueens
from problems.problem import Problem
from problems.traveling_salesman import TravelingSalesman


class Solver:
    def __init__(self, problem: Problem, init_state: tuple):
        self.__problem = problem
        self.__state = init_state
        self.__val = problem.evaluate(init_state)

    def __call__(self):
        opt = self.__problem.opt
        while self.run():
            changed = False
            neighbors = self.__problem.neighbors(self.__state)
            shuffle(neighbors)
            for neighbor in neighbors:
                val = self.__problem.evaluate(neighbor)
                if val == opt(val, self.__val):
                    self.__val = val
                    self.__state = neighbor
                    changed = True
                    print(self.__state, pr.evaluate(self.__state))
                    # pr.show(self.__state)
                    break
            if not changed:
                return self.__state

    def run(self):
        return True


if __name__ == '__main__':
    print('running')
    # pr = TravelingSalesman()
    # cities = ((1,9), (3,7), (5,10), (7,11), (5,3), (3,2), (0,4), (6,9), (27,12), (15,23), (43, 1), (22, 17), (1, 23), (11, 10), (21,2))
    # s = Solver(pr, cities)
    # solution = s()
    # print(pr.evaluate(solution))

    n = 8
    pr = NQueens(n)
    init = tuple(i for i in range(n))
    s = Solver(pr, init)
    solution = s()
    print(pr.evaluate(solution))
    pr.show(solution)
