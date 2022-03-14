from collections import deque
from math import inf

from solvers import Solver


class TabuSearch(Solver):
    def __init__(self, problem, init_state, max_iterations: int, tabu_list_size: int, batch_size=inf):
        super().__init__(problem, init_state, batch_size, max_iterations=max_iterations)
        self._tabu_list = deque([init_state], tabu_list_size)

    def choose_best_from_batch(self, neighbors):
        legal_neighbors = [neighbor for neighbor in neighbors if neighbor not in self._tabu_list]
        if not legal_neighbors:
            return None
        return super().choose_best_from_batch(legal_neighbors)

    def is_preferred_state(self, state, val) -> bool:
        return bool(state)

    def state_changed(self):
        self._tabu_list.append(self._state)


class TabuSearchSourceCode:
    # https://towardsdatascience.com/optimization-techniques-tabu-search-36f197ef8e25
    def __init__(self, initialSolution, solutionEvaluator, neighborOperator, aspirationCriteria,
                 acceptableScoreThreshold, tabuTenure):
        self.currSolution = initialSolution
        self.bestSolution = initialSolution
        self.evaluate = solutionEvaluator
        self.aspirationCriteria = aspirationCriteria
        self.neighborOperator = neighborOperator
        self.acceptableScoreThreshold = acceptableScoreThreshold
        self.tabuTenure = tabuTenure

    def isTerminationCriteriaMet(self):
        # can add more termination criteria
        return self.evaluate(self.bestSolution) < self.acceptableScoreThreshold \
               or self.neighborOperator(self.currSolution) == 0

    def run(self):
        tabuList = {}

        while not self.isTerminationCriteriaMet():
            # get all of the neighbors
            neighbors = self.neighborOperator(self.currSolution)
            # find all tabuSolutions other than those
            # that fit the aspiration criteria
            tabuSolutions = tabuList.keys()
            # find all neighbors that are not part of the Tabu list
            neighbors = filter(lambda n: self.aspirationCriteria(n), neighbors)
            # pick the best neighbor solution
            newSolution = sorted(neighbors, key=lambda n: self.evaluate(n))[0]
            # get the cost between the two solutions
            cost = self.evaluate(self.solution) - self.evaluate(newSolution)
            # if the new solution is better,
            # update the best solution with the new solution
            if cost >= 0:
                self.bestSolution = newSolution
            # update the current solution with the new solution
            self.currSolution = newSolution

            # decrement the Tabu Tenure of all tabu list solutions
            for sol in tabuList:
                tabuList[sol] -= 1
                if tabuList[sol] == 0:
                    del tabuList[sol]
            # add new solution to the Tabu list
            tabuList[newSolution] = self.tabuTenure

        # return best solution found
        return self.bestSolution

