from collections import defaultdict
from random import shuffle
from typing import Tuple, Union
import matplotlib.pyplot as plt

from problems.problem import Problem
import numpy as np


class NQueens(Problem):
    def __init__(self, n: int):
        self.__n = n

    @property
    def opt(self) -> Union[max, min]:
        return min

    def neighbors(self, state):
        neighbors = []
        for i, j in enumerate(state):
            l_state = list(state)
            for new_j in range(self.__n):
                if new_j != j:
                    l_state[i] = new_j
                    neighbors.append(tuple(l_state))
        return neighbors

    def evaluate(self, state: tuple):
        queens = []
        threats = 0
        for new_queen in enumerate(state):
            assert 0 <= new_queen[1] < self.__n
            for queen in queens:
                if self.__threat(new_queen, queen):
                    threats += 1
            queens.append(new_queen)
        return threats

    @staticmethod
    def __threat(q1: Tuple[int, int], q2: Tuple[int, int]):
        return q1[0] == q2[0] or q1[1] == q2[1] or q1[0]-q1[1] == q2[0]-q2[1] or q1[0]+q1[1] == q2[0]+q2[1]

    def show(self, state):
        # Make a 9x9 grid...
        nrows, ncols = 9, 9
        board = np.zeros((self.__n, self.__n))

        # Reshape things into a 9x9 grid.
        for i, j in enumerate(state):
            board[i][j] = 1

        row_labels = range(self.__n)
        col_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        plt.matshow(board)
        plt.xticks(range(self.__n), col_labels)
        plt.yticks(range(self.__n), row_labels)
        plt.show()
        # n = self.__n
        # for i in state:
        #     line = ''
        #     for j in range(n):
        #         line += 'X' if j == i else '_'
        #     print(line)


if __name__ == '__main__':
    print(NQueens(4).evaluate((2, 0, 3, 1)))
