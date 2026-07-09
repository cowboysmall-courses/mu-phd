import random

from typing import List, Tuple
from utils.functions import repeat_function


"""

    This module contains utility functions for constructing DNA strings

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


BASES    = ['A', 'G', 'C', 'T']
PAIRINGS = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}


def generate_strand(length: int) -> str:
    """

        generates a random strand of specific length from the bases

        Parameters
        ----------
        length: int
            the lenght of the generated strand

        Returns
        -------
        str
            the generated strand

    """
    return ''.join(random.choices(BASES, k=length))


def create_vertex_strands(length: int, count: int) -> List[str]:
    """

        creates a specified number of vertex strands of specific length

        Parameters
        ----------
        length: int
            the lenght of the generated vertex strands
        count: int
            the number of the generated vertex strands

        Returns
        -------
        List[str]
            the generated vertex strands

    """
    return repeat_function(generate_strand, count, length)


def complement_strand(strand: str) -> str:
    """

        creates the complement of a strand

        Parameters
        ----------
        strand: str
            the strand to find the complement of

        Returns
        -------
        str
            the complement of the strand

    """
    return ''.join(PAIRINGS[c] for c in strand)


def complement_strands(strands: List[str]) -> List[str]:
    """

        creates the complement of a list of strand

        Parameters
        ----------
        strands: List[str]
            the list of strands to find the complement of

        Returns
        -------
        List[str]
            the list of complements of the list of strands

    """
    return [complement_strand(strand) for strand in strands]


def create_edge_strands(strands: List[str], edges: List[Tuple], length: int) -> List[str]:
    """

        creates a specified number of edge strands from the edges

        Parameters
        ----------
        strands: List[str]
            the list of vertex strands to construct the edge strands from
        edges: List[Tuple]
            the edges of the graph
        length: int
            the lenght of a vertex strand

        Returns
        -------
        List[str]
            the list of edge strands

    """
    return [strands[v1][-(length//2):] + strands[v2][:(length//2)] for (v1, v2) in edges]


def create_paths(vertex_strands: List[str], edge_strands: List[str], in_strand: str, out_strand: str, length: int) -> List[List[str]]:
    """

        create paths from a list of vertex strands according to the provided edge strands

        Parameters
        ----------
        vertex_strands: List[str]
            the list of vertex strands
        edge_strands: List[str]
            the list of edge strands
        in_strand: str
            the in strand
        out_strand: str
            the out strand
        length: int
            the lenght of a vertex strand

        Returns
        -------
        List[List[str]]
            the list of paths


    """
    paths = []
    edges = set(edge_strands)

    path  = [in_strand]
    for strand in vertex_strands:
        edge = complement_strand(path[-1][-(length//2):] + strand[:(length//2)])
        if edge in edges:
            path.append(strand)

        if path[-1] == out_strand:
            paths.append(path)
            path = [in_strand]

    return paths

