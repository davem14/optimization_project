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
        l_state = list(state)
        l = len(state)
        neighbors = []
        for i in range(l):
            for j in range(i, l):
                if i == j:
                    continue
                l_state[i], l_state[j] = l_state[j], l_state[i]
                neighbors.append(tuple(l_state))
                l_state[i], l_state[j] = l_state[j], l_state[i]
        return neighbors

    @property
    def opt(self) -> Union[max, min]:
        return min

    def show(self, state):
        xs, ys = zip(*state + (state[0],))  # create lists of x and y values
        plt.plot(xs, ys, 'go-')
        plt.pause(0.01)
        plt.clf()
