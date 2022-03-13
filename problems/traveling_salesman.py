import random
from typing import Union

from matplotlib import pyplot as plt

from problems.problem import Problem


class TravelingSalesman(Problem):

    @staticmethod
    def __euclid_dist(p1, p2):
        return sum((x-y)**2 for x, y in zip(p1, p2)) ** 0.5

    def evaluate(self, state):
        return sum(self.__euclid_dist(p1, p2) for p1, p2 in zip(state, state[1:] + (state[0],)))

    def neighbors(self, state):
        index_list = list(range(len(state)))
        random.shuffle(index_list)
        length = len(state) - 1
        for i in index_list:
            l_state = list(state)
            point = l_state.pop(i)
            for j in range(i+1, i-1+length):
                j %= length
                yield tuple(l_state[:j] + [point] + l_state[j:])

    @property
    def opt(self) -> Union[max, min]:
        return min

    def show(self, state):
        xs, ys = zip(*state + (state[0],))  # create lists of x and y values
        plt.plot(xs, ys, 'go-')
        plt.pause(0.01)
        plt.clf()
