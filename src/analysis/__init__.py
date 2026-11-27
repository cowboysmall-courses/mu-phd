
from typing import List

from pathlib import Path

from scipy import stats
from seaborn.objects import Plot

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd


def plot_result(energy: List[float], path:str, name: str, title: str = "Title") -> None:
    Path(f"./output/analysis/dna/{path}").mkdir(parents = True, exist_ok = True)

    plt.style.use("ggplot")
    plt.subplots(figsize = (12, 5))

    plt.title(title)
    plt.grid(True)
    plt.xlabel("Position")
    plt.ylabel("Free Energy")
    plt.plot(energy, label = "Energy")
    plt.legend()

    plt.savefig(f"./output/analysis/dna/{path}/{name}_plot.png")
    plt.close()


def plot_results(results1: List[float], results2: List[float], label1: str, label2:str, path:str, name: str, title: str = "Title") -> None:
    Path(f"./output/analysis/dna/{path}").mkdir(parents = True, exist_ok = True)

    plt.style.use("ggplot")
    plt.subplots(figsize = (12, 5))

    plt.title(title)
    plt.grid(True)
    plt.xlabel("Position")
    plt.ylabel("Free Energy")
    plt.plot(results1, color = "red",  label = label1)
    plt.plot(results2, color = "blue", label = label2)
    plt.legend()

    plt.savefig(f"./output/analysis/dna/{path}/{name}_plot.png")
    plt.close()


def plot_results_separately(results1: List[float], results2: List[float], label1: str, label2:str, path:str, name: str, title: str = "Title") -> None:
    Path(f"./output/analysis/dna/{path}").mkdir(parents = True, exist_ok = True)

    plt.style.use("ggplot")
    fig, (ax1, ax2) = plt.subplots(2, figsize = (12, 5))

    fig.suptitle(title)

    ax1.grid(True)
    # ax1.xlabel("Position")
    # ax1.ylabel("Free Energy")
    ax1.plot(results1, label = label1)
    ax1.legend()

    ax2.grid(True)
    # ax2.xlabel("Position")
    # ax2.ylabel("Free Energy")
    ax2.plot(results2, label = label2)
    ax2.legend()

    plt.savefig(f"./output/analysis/dna/{path}/{name}_plot.png")
    plt.close()



def hist_result(energy: List[float], path:str, name: str, title: str = "Title") -> None:
    Path(f"./output/analysis/dna/{path}").mkdir(parents = True, exist_ok = True)

    plt.style.use("ggplot")
    plt.subplots(figsize = (12, 5))

    plt.title(title)
    plt.grid(True)
    plt.ylabel("Free Energy")

    plt.hist(energy, bins = 5, label = "Energy Distribution", density = True)

    plt.savefig(f"./output/analysis/dna/{path}/{name}_hist.png")
    plt.close()



def dist_result(energy: List[float], path:str, name: str, title: str = "Title") -> None:
    Path(f"./output/analysis/dna/{path}").mkdir(parents = True, exist_ok = True)

    plt.style.use("ggplot")
    plt.subplots(figsize = (12, 5))
    Plot().layout(size = (12, 5))

    plt.title(title)
    plt.grid(True)
    plt.ylabel("Free Energy")

    # nrg = np.array(energy, dtype = np.float32)
    nrg = pd.DataFrame(energy, columns = ["Energy"])
    sns.displot(nrg, x = "Energy", kind = "kde")

    plt.savefig(f"./output/analysis/dna/{path}/{name}_dist.png")
    plt.close()


