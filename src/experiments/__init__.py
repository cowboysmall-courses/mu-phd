

class Simulation:

    def __init__(self, data: dict):
        self._data = data

    def pre(self, iteration: int, data: dict) -> None:
        pass

    def simulate(self, iteration: int, data: dict) -> None:
        pass

    def post(self, iteration: int, data: dict) -> None:
        pass

    def run(self, iterations: int):
        try:
            for iteration in range(iterations):
                self.pre(iteration, self._data)
                self.simulate(iteration, self._data)
                self.post(iteration, self._data)
        except SimulationException:
            pass

        return self._data


class SimulationException(Exception):
    pass
