
from typing import Dict

import logging


class Simulation:

    def __init__(self):
        logging.basicConfig()
        self._logger = logging.getLogger(__name__)
        self._logger.setLevel(logging.INFO)


    def pre_run(self, data: Dict) -> None:
        self._logger.info(">>> pre_run")

    def pre_simulate(self, iteration: int, data: Dict) -> None:
        self._logger.info(">>> pre_simulate")

    def pre_step(self, iteration: int, timestep: int, data: Dict) -> None:
        self._logger.info(">>> pre_step")

    def step(self, iteration: int, timestep: int, data: Dict) -> None:
        pass

    def post_step(self, iteration: int, timestep: int, data: Dict) -> None:
        self._logger.info(">>> post_step")

    def post_simulate(self, iteration: int, data: Dict) -> None:
        self._logger.info(">>> post_simulate")

    def post_run(self, data: Dict) -> None:
        self._logger.info(">>> post_run")

    def run(self, iterations: int, timesteps: int, data: Dict = {}) -> Dict:
        self.pre_run(data)
        try:
            for iteration in range(iterations):
                self._logger.info(f">>> iteration {iteration + 1}")
                self.pre_simulate(iteration, data)
                self.__simulate(iteration, timesteps, data)
                self.post_simulate(iteration, data)
        except SimulationException:
            pass
        self.post_run(data)
        return data

    def __simulate(self, iteration: int, timesteps: int, data: Dict) -> None:
        for timestep in range(timesteps):
            self._logger.info(f">>> iteration {iteration + 1} - timestep {timestep + 1}")
            self.pre_step(iteration, timestep, data)
            self.step(iteration, timestep, data)
            self.post_step(iteration, timestep, data)



class SimulationException(Exception):
    pass


