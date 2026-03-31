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

## A Brief Note on the Simulation of Adleman's Experiment

This simulation demonstrates solving the Traveling Salesman problem through DNA computing as follows:

1. we take a simple graph
2. we encode the vertices as DNA molecules
3. we encode the edges as DNA molecules
4. we allow the vertices to bind randomly according to the edges
5. we retain for consideration only candidate molecules that fulfill the criteria

If there are any remaining molecules then we have a solution, otherwise we do not have a solution.

## References

### Papers

- [Molecular Computation of Solutions to Combinatorial Problems](https://www.cs.unc.edu/~montek/teaching/Comp790-Fall11/Home/Home_files/Adleman-Science94.pdf)
- [Molecular Computing: from Conformational Pattern Recognition to Complex Processing Networks](https://eprints.soton.ac.uk/261898/1/ConradM96ConfPttrRecCplxProcNet.pdf)
- [The Art of Molecular Computing](https://arxiv.org/pdf/2102.06629)
- [Molecular Computing: Paths to Chemical Turing Machines](https://pdfs.semanticscholar.org/568f/da26437fd3c632de834a24fd202f1a77bd48.pdf)
- [Advances in Molecular Programming and Computing](https://www.dna.caltech.edu/Papers/Denmark_Workshop_2013.pdf)
- [From Molecular Computing to Molecular Programming](https://www.cs.auckland.ac.nz/~cristian/UMCreadings/dnaprogramming.pdf)
- [DNA Molecule Provides a Computing Machine with both Data and Fuel](https://courses.cs.duke.edu/cps296.4/spring04/papers/BAPLS03.pdf)
- [Biomolecular Computing and Programming](https://scispace.com/pdf/biomolecular-computing-and-programming-2if8v4lqko.pdf)
- [A Thermodynamically Favoured Molecular Computer](https://www.biorxiv.org/content/10.1101/2025.07.16.664196v1)
- [Molecular Computing and Bioinformatics](https://www.researchgate.net/publication/334044489_Molecular_Computing_and_Bioinformatics)

### Presentations

- [Introduction to Molecular Computing](https://ocw.u-tokyo.ac.jp/lecture_files/sci_01/2/notes/en/mc-tutorial_e.pdf)
- [Molecular Computing](https://www.wishartlab.com/system/resources/W1siZiIsIjIwMTMvMTAvMjEvMTlfMDdfMzRfNDE2XzQ5NV9MZWN0NF8xLnBkZiJdXQ/495-Lect4-1.pdf)
- [Modeling Molecular Motions](https://www.wishartlab.com/system/resources/W1siZiIsIjIwMTMvMTAvMjEvMTZfMTJfMDZfOTc1XzQ5NV9MZWN0NS5wZGYiXV0/495-Lect5.pdf)
- [Tutorial on Molecular Computing](https://www.iiitb.ac.in/csl/events/conference/ramanujan/rmit09/website09/slides/Dr%20Balan.pdf)

### Videos

- [The Math Behind Building An AI Using DNA](https://www.youtube.com/watch?v=0luZ4JqHg6w)
- [DNA Computing 101: How can DNA do computations?](https://www.youtube.com/watch?v=YBhWrHeIqDs)
