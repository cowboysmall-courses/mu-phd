# Molecular Computing

Collected research and simulations on Molecular / DNA computing

## Setup

Clone the repository as follows:

```

> git clone git@github.com:cowboysmall-courses/mu-phd.git


```

and then move into the root of the repository:

```

> cd mu-phd/


```

ensure that [uv](https://docs.astral.sh/uv/getting-started/installation/) is installed, and then run the following:

```

> uv run adleman


```

you should see output similar to the below:

```

    A Simulation of Adleman's Experiiment:


  Original Vertices: 0, 1, 2, 3, 4, 5, 6
     Original Edges: 0 -> 1, 0 -> 3, 0 -> 6, 1 -> 2, 1 -> 3, 2 -> 1, 2 -> 3, 3 -> 2, 3 -> 4, 4 -> 1, 4 -> 5, 5 -> 1, 5 -> 2, 5 -> 6


   Encoded Vertices: TTAAAACTTTGCTAGGCTGA, TTCGCCCATATACCAGAACC, TAGCACCACGGTTACTGAAG, GGATCGGGCCACTATCCCCA, CAAACAAAAGGGCCATCATG, AAGAGAGGTTTTTCAGGGGC, GTCTTGTGCGGCATCCAGCA
        Complements: AATTTTGAAACGATCCGACT, AAGCGGGTATATGGTCTTGG, ATCGTGGTGCCAATGACTTC, CCTAGCCCGGTGATAGGGGT, GTTTGTTTTCCCGGTAGTAC, TTCTCTCCAAAAAGTCCCCG, CAGAACACGCCGTAGGTCGT
      Encoded Edges: CGATCCGACTAAGCGGGTAT, CGATCCGACTCCTAGCCCGG, CGATCCGACTCAGAACACGC, ATGGTCTTGGATCGTGGTGC, ATGGTCTTGGCCTAGCCCGG, CAATGACTTCAAGCGGGTAT, CAATGACTTCCCTAGCCCGG, TGATAGGGGTATCGTGGTGC, TGATAGGGGTGTTTGTTTTC, CCGGTAGTACAAGCGGGTAT, CCGGTAGTACTTCTCTCCAA, AAAGTCCCCGAAGCGGGTAT, AAAGTCCCCGATCGTGGTGC, AAAGTCCCCGCAGAACACGC


             Step 1:  6789 Paths Found
             Step 2:  6789 Paths Found
             Step 3:   106 Paths Found
             Step 4:    49 Paths Found
             Step 5: Yes


 Encoded Path Found: TTAAAACTTTGCTAGGCTGA -> TTCGCCCATATACCAGAACC -> TAGCACCACGGTTACTGAAG -> GGATCGGGCCACTATCCCCA -> CAAACAAAAGGGCCATCATG -> AAGAGAGGTTTTTCAGGGGC -> GTCTTGTGCGGCATCCAGCA
         Path Found: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6


```

## The Simulation of Adleman's Experiment

This simulation demonstrates solving the Traveling Salesman problem through DNA computing as follows:

1. we take a simple graph
2. we encode the vertices as DNA molecules
3. we encode the edges as DNA molecules
4. we allow them to bind randomly
5. we retain for consideration only candidate molecules that fulfill the criteria

If there are any remaining molecules then we have a solution, otherwise we do not have a solution.
