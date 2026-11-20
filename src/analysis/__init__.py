
from typing import List, Dict

from pathlib import Path

from scipy import stats
from seaborn.objects import Plot

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd


def plot_results(energy: List[float], path:str, name: str, title: str = "Title") -> None:
    Path(f"./output/analysis/dna/{path}").mkdir(parents = True, exist_ok = True)

    plt.style.use("ggplot")
    plt.subplots(figsize = (12, 5))

    plt.title(title)
    plt.grid(True)
    plt.xlabel("Position")
    plt.ylabel("Gibbs Free Energy")
    plt.plot(energy, label = "Energy Landscape")
    plt.legend()

    plt.savefig(f"./output/analysis/dna/{path}/{name}_plot.png")
    plt.close()


def hist_results(energy: List[float], path:str, name: str, title: str = "Title") -> None:
    Path(f"./output/analysis/dna/{path}").mkdir(parents = True, exist_ok = True)

    plt.style.use("ggplot")
    plt.subplots(figsize = (12, 5))

    plt.title(title)
    plt.grid(True)
    # plt.xlabel("Position")
    plt.ylabel("Gibbs Free Energy")

    plt.hist(energy, bins = 5, label = "Energy Landscape Distribution", density = True)

    plt.savefig(f"./output/analysis/dna/{path}/{name}_hist.png")
    plt.close()



def dist_results(energy: List[float], path:str, name: str, title: str = "Title") -> None:
    Path(f"./output/analysis/dna/{path}").mkdir(parents = True, exist_ok = True)

    plt.style.use("ggplot")
    plt.subplots(figsize = (12, 5))
    Plot().layout(size = (12, 5))

    plt.title(title)
    plt.grid(True)
    # plt.xlabel("Position")
    plt.ylabel("Gibbs Free Energy")

    # nrg = np.array(energy, dtype = np.float32)
    nrg = pd.DataFrame(energy, columns = ["Energy Landscape"])
    sns.displot(nrg, x = "Energy Landscape", kind = "kde")
    # plt.legend()

    plt.savefig(f"./output/analysis/dna/{path}/{name}_dist.png")
    plt.close()


