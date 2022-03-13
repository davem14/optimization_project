from collections import deque

from problems import Problem
from solvers import Solver


class TabuSearch(Solver):
    def __init__(self, problem: Problem, init_state: tuple, max_size: int):
        super().__init__(problem, init_state)
        self._tabu_list = deque([init_state], max_size)

    def is_preferred_state(self, state, val) -> bool:
        pass

    def state_changed(self):
        pass

# class TabuSearchSourceCode:
#     # https://towardsdatascience.com/optimization-techniques-tabu-search-36f197ef8e25
#     def __init__(self, initialSolution, solutionEvaluator, neighborOperator, aspirationCriteria,
#                  acceptableScoreThreshold, tabuTenure):
#         self.currSolution = initialSolution
#         self.bestSolution = initialSolution
#         self.evaluate = solutionEvaluator
#         self.aspirationCriteria = aspirationCriteria
#         self.neighborOperator = neighborOperator
#         self.acceptableScoreThreshold = acceptableScoreThreshold
#         self.tabuTenure = tabuTenure
#
#     def isTerminationCriteriaMet(self):
#         # can add more termination criteria
#         return self.evaluate(self.bestSolution) < self.acceptableScoreThreshold \
#                or self.neighborOperator(self.currSolution) == 0
#
#     def run(self):
#         tabuList = {}
#
#         while not self.isTerminationCriteriaMet():
#             # get all of the neighbors
#             neighbors = self.neighborOperator(self.currSolution)
#             # find all tabuSolutions other than those
#             # that fit the aspiration criteria
#             tabuSolutions = tabuList.keys()
#             # find all neighbors that are not part of the Tabu list
#             neighbors = filter(lambda n: self.aspirationCriteria(n), neighbors)
#             # pick the best neighbor solution
#             newSolution = sorted(neighbors, key=lambda n: self.evaluate(n))[0]
#             # get the cost between the two solutions
#             cost = self.evaluate(self.solution) - self.evaluate(newSolution)
#             # if the new solution is better,
#             # update the best solution with the new solution
#             if cost >= 0:
#                 self.bestSolution = newSolution
#             # update the current solution with the new solution
#             self.currSolution = newSolution
#
#             # decrement the Tabu Tenure of all tabu list solutions
#             for sol in tabuList:
#                 tabuList[sol] -= 1
#                 if tabuList[sol] == 0:
#                     del tabuList[sol]
#             # add new solution to the Tabu list
#             tabuList[newSolution] = self.tabuTenure
#
#         # return best solution found
#         return self.bestSolution

