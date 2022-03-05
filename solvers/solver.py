from random import shuffle

from problems.problem import Problem


class Solver:
    def __init__(self, problem: Problem, init_state: tuple):
        self.__problem = problem
        self.__state = init_state
        self.__values = [problem.evaluate(init_state)]
        self._running = True

    def __call__(self):
        opt = self.__problem.opt
        while self._running:
            changed = False
            neighbors = self.__problem.neighbors(self.__state)
            shuffle(neighbors)
            for neighbor in neighbors:
                neighbor_val = self.__problem.evaluate(neighbor)
                if neighbor_val == opt(neighbor_val, self.__values[-1]):
                    self.__values.append(neighbor_val)
                    self.__state = neighbor
                    changed = True
                    print(self.__state, neighbor_val)
                    self.__problem.show(self.__state)
                    break
            if not changed:
                return self.__state
