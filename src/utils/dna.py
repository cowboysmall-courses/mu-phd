
import random

from typing import List


"""

    This module contains utility functions for working with DNA strands

    DNA Bases:
        A - Adenine
        C - Cytosine
        G - Guanine
        T - Thymine

    Pairings:
        A -> T
        T -> A
        C -> G
        G -> C

"""



BASES = ["A", "G", "C", "T"]
COMP  = {"A": "T", "T": "A", "C": "G", "G": "C"}


def generate_strand(length: int) -> str:
    """

        generates a random strand of specific length from the bases

        Parameters
        ----------
        length: int
            the length of the generated strand

        Returns
        -------
        str
            the generated strand

    """
    return ''.join(random.choices(BASES, k=length))



def complement(strand: str) -> str:
    """

        creates the complement of a strand of DNA

        Parameters
        ----------
        strand: str
            the strand to find the complement of

        Returns
        -------
        str
            the complement of the strand

    """
    return "".join(COMP[N] for N in strand)



def reverse_complement(strand: str) -> str:
    """

        creates the reverse complement of a strand of DNA

        Parameters
        ----------
        strand: str
            the strand to find the reverse complement of

        Returns
        -------
        str
            the reverse complement of the strand

    """
    return "".join(COMP[N] for N in strand)[::-1]



def complements(strands: List[str]) -> List[str]:
    """

        creates the complements of a list of strands

        Parameters
        ----------
        strands: List[str]
            the list of strands to find the complements of

        Returns
        -------
        List[str]
            the list of complements of the list of strands

    """
    return [complement(strand) for strand in strands]



def reverse_complements(strands: List[str]) -> List[str]:
    """

        creates the reverse complements of a list of strands

        Parameters
        ----------
        strands: List[str]
            the list of strands to find the reverse complements of

        Returns
        -------
        List[str]
            the list of reverse complements of the list of strands

    """
    return [reverse_complement(strand) for strand in strands]




def is_self_complementary(strand: str) -> bool:
    """

        determines if a strand is self-complementary

        Parameters
        ----------
        strand: str
            the strand to determine if self-complementary

        Returns
        -------
        bool
            true if the strand is self-complementary

    """
    return strand == reverse_complement(strand)



def read_dna_from_file(path: str) -> str:
    """

        reads a dna string from a file

        Parameters
        ----------
        path: str
            the path to the file

        Returns
        -------
        str
            the dna string

    """
    lines = []

    with open(path, "r") as file:
        for line in file:
            lines.append(line.strip())

    return "".join(lines)

