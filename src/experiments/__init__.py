
from typing import Dict

class Simulation:

    def pre_run(self, data: Dict) -> None:
        pass

    def pre_simulate(self, iteration: int, data: Dict) -> None:
        pass

    def pre_step(self, iteration: int, timestep: int, data: Dict) -> None:
        pass

    def step(self, iteration: int, timestep: int, data: Dict) -> None:
        pass

    def post_step(self, iteration: int, timestep: int, data: Dict) -> None:
        pass

    def post_simulate(self, iteration: int, data: Dict) -> None:
        pass

    def post_run(self, data: Dict) -> None:
        pass

    def __simulate(self, iteration: int, timesteps: int, data: Dict) -> None:
        for timestep in range(timesteps):
            self.pre_step(iteration, timestep, data)
            self.step(iteration, timestep, data)
            self.post_step(iteration, timestep, data)

    def run(self, iterations: int, timesteps: int, data: Dict = {}) -> Dict:
        self.pre_run(data)
        try:
            for iteration in range(iterations):
                self.pre_simulate(iteration, data)
                self.__simulate(iteration, timesteps, data)
                self.post_simulate(iteration, data)
        except SimulationException:
            pass
        self.post_run(data)
        return data


class SimulationException(Exception):
    pass
