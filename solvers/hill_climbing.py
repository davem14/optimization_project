from solvers import Solver


class HillClimbing(Solver):
    def state_changed(self):
        pass

    def is_preferred_state(self, val) -> bool:
        return val >= 0
