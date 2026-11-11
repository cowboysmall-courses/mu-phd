
from utils.simulations import Simulation, SimulationException

from typing import Callable, Dict, Generator, List, Tuple

from sdc.scaffold import Scaffold
from sdc.tile import Tile


class SDCSimulation(Simulation):

    def __init__(self, scaffold: Scaffold, tileset: List[List[Tile]]):
        super().__init__()
        self._scaffolds = [Scaffold(len(solution)) for _ in range(scaffolds)]


    def step(self, iteration: int, timestep: int, data: Dict) -> None:



def main() -> None:
    SDCSimulation().run(2, 10)


