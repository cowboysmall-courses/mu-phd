# SDC Experiment - Bind / Replace

## Description

This simulation demonstrates solving a problem through SDC:

1. for each scaffold, randomly pick a tile from the solution
    - place if the tile's position is vacant
    - replace if mismatches are less than or equal to the existing tile
    - otherwise continue
2. continue until experiment concludes
3. collect completed scaffolds, and count successes
4. report on the outcome

## Running the Experiment

Ensure that [uv](https://docs.astral.sh/uv/getting-started/installation/) is installed, and then run the following:

```zsh

> uv run exp-sdc-br-bitcopy

```

you should see output similar to the below:

```

    A Simulation of Scaffolded DNA Computer - Bind / Replace: Bitcopy


    Results after 5 iterations

     Iteration: 1
         Total: 4994
    Proportion: 99.88%

     Iteration: 2
         Total: 4995
    Proportion: 99.90%

     Iteration: 3
         Total: 4999
    Proportion: 99.98%

     Iteration: 4
         Total: 4995
    Proportion: 99.90%

     Iteration: 5
         Total: 4995
    Proportion: 99.90%


```

## Notes

For further research some or all of the following need to be taken into consideration:

1. The state of the system is dictated by energy / temperature according to the Boltzman distribution
