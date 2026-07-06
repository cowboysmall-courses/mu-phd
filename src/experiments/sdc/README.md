# SDC Experiment

## Description

This simulation demonstrates solving a problem through SDC:

1. for each scaffold, randomly pick a tile from the solution
    - if the tile position is vacant, place it and proceed
    - replace (probability) the existing tile if the bind is imperfect
    - otherwise continue from the beginning with the next scaffold
2. continue until experiment concludes
3. collect completed scaffolds, and count successes
4. report on the outcome

## Running the Experiment

Ensure that [uv](https://docs.astral.sh/uv/getting-started/installation/) is installed, and then run the following:

```zsh

> uv run exp-sdc-parity

```

you should see output similar to the below:

```

    A Simulation of Scaffolded DNA Computer: Parity


    Results after 10 iterations

     Iteration: 1
         Count: 6264
    Proportion: 62.64%

     Iteration: 2
         Count: 6428
    Proportion: 64.28%

     Iteration: 3
         Count: 6137
    Proportion: 61.37%

     Iteration: 4
         Count: 6381
    Proportion: 63.81%

     Iteration: 5
         Count: 6139
    Proportion: 61.39%

     Iteration: 6
         Count: 5519
    Proportion: 55.19%

     Iteration: 7
         Count: 6133
    Proportion: 61.33%

     Iteration: 8
         Count: 5964
    Proportion: 59.64%

     Iteration: 9
         Count: 5822
    Proportion: 58.22%

     Iteration: 10
         Count: 6511
    Proportion: 65.11%



```

## Notes

For further research some or all of the following need to be taken into consideration:

1. If left unattended, the temperature in the container falls according to Newton's Law of Cooling
2. The state of the system is dictated by energy / temperature according to the Boltzman distribution
