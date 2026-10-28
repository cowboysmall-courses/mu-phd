
from sdc.tile import Tile
from sdc import k_f, R_j

from utils.dna import is_self_complementary

import math


WCDB = {
    ("AA", "TT"):  (-7.6, -21.3), ("TT", "AA"):  (-7.6, -21.3),
    ("AT", "TA"):  (-7.2, -20.4), ("TA", "AT"):  (-7.2, -21.3),
    ("CA", "GT"):  (-8.5, -22.7), ("TG", "AC"):  (-8.5, -22.7),
    ("GT", "CA"):  (-8.4, -22.4), ("AC", "TG"):  (-8.4, -22.4),
    ("CT", "GA"):  (-7.8, -21.0), ("AG", "TC"):  (-7.8, -21.0),
    ("GA", "CT"):  (-8.2, -22.2), ("TC", "AG"):  (-8.2, -22.2),
    ("CG", "GC"): (-10.6, -27.2), ("GC", "CG"):  (-9.8, -24.4),
    ("GG", "CC"):  (-8.0, -19.9), ("CC", "GG"):  (-8.0, -19.9)
}

MMDB = {

    ("GA", "CA"):  0.17, ("GA", "CC"):  0.81, ("GA", "CG"): -0.25,
    ("GC", "CA"):  0.47, ("GC", "CC"):  0.79, ("GC", "CT"):  0.62,
    ("GG", "CA"): -0.52, ("GG", "CG"): -1.11, ("GG", "CT"):  0.08,
    ("GT", "CC"):  0.98, ("GT", "CG"): -0.59, ("GT", "CT"):  0.45,

    ("CA", "GA"):  0.43, ("CA", "GC"):  0.75, ("CA", "GG"):  0.03,
    ("CC", "GA"):  0.79, ("CC", "GC"):  0.70, ("CC", "GT"):  0.62,
    ("CG", "GA"):  0.11, ("CG", "GG"): -0.11, ("CG", "GT"): -0.47,
    ("CT", "GC"):  0.40, ("CT", "GG"): -0.32, ("CT", "GT"): -0.12,

    ("AA", "TA"):  0.61, ("AA", "TC"):  0.88, ("AA", "TG"):  0.14,
    ("AC", "TA"):  0.77, ("AC", "TC"):  1.33, ("AC", "TT"):  0.64,
    ("AG", "TA"):  0.02, ("AG", "TG"): -0.13, ("AG", "TT"):  0.71,
    ("AT", "TC"):  0.73, ("AT", "TG"):  0.07, ("AT", "TT"):  0.69,

    ("TA", "AA"):  0.69, ("TA", "AC"):  0.92, ("TA", "AG"):  0.42,
    ("TC", "AA"):  1.33, ("TC", "AC"):  1.05, ("TC", "AT"):  0.97,
    ("TG", "AA"):  0.74, ("TG", "AG"):  0.44, ("TG", "AT"):  0.43,
    ("TT", "AC"):  0.75, ("TT", "AG"):  0.34, ("TT", "AT"):  0.68,
}

ATTA = {("A", "T"), ("T", "A")}

INIT = (0.2, -5.7)
SYMC = (0,   -1.4)
TATP = (2.2,  6.9)


def rate_attach(tile: Tile) -> float:
    """

        calculate the attachment rate

        Parameters
        ----------
        concentration: int
            the tile concentration

        Returns
        -------
        float
            the attachment rate

    """
    return k_f * tile.get_concentration()



def rate_detach(left: Tile, tile: Tile, right: Tile, T: float) -> float:
    """

        calculate the detachment rate

        Parameters
        ----------
        left: Tile
            the tile to the left of the current tile
        tile: Tile
            the current tile
        right: Tile
            the tile to the right of the current tile
        T: float
            the temperature in Kelvin

        Returns
        -------
        float
            the detachment rate

    """
    return k_f * math.exp( (gibbs_rl(left, tile, T) + gibbs_m(tile, T) + gibbs_rl(tile, right, T)) / (R_j * T) )



def gibbs_rl(tile_left: Tile, tile_right: Tile, T: float) -> float:
    """

        calculates the Gibbs Free Energy of binding two compute
        domains of consecutive tiles

        Parameters
        ----------
        tile_left: Tile
            the first tile
        tile_right: Tile
            the second tile
        T: float
            the temperature in Kelvin

        Returns
        -------
        float
            the Gibbs Free Energy of binding

    """
    return 0 if tile_right.left() == "" else free_energy(tile_left.right(), tile_right.left()[::-1], T)


def gibbs_m(tile: Tile, T: float) -> float:
    """

        calculates the Gibbs Free Energy of binding to a
        scaffold domains

        Parameters
        ----------
        tile: Tile
            the tile to bind to the scaffold
        T: float
            the temperature in Kelvin

        Returns
        -------
        float
            the Gibbs Free Energy of binding

    """
    return 0 if tile.middle() == "" else free_energy(tile.middle(), tile.middle_c(), T)


def gibbs_assoc(T:float) -> float:
    """

        calculates the Gibbs Free Energy of association

        Parameters
        ----------
        T: float
            the temperature in Kelvin

        Returns
        -------
        float
            the Gibbs Free Energy of association

    """
    return 0



def free_energy(S1: str, S2: str, T: float) -> float:
    """

        calculates the Gibbs Free Energy of two strands using
        the folowing database of values associated with nearest neighbours:

                                        D_H                 D_S             D_G

                                Kcal mol^-1     cal K^-1 mol^-1     kcal mol^-1

            AA/TT                      −7.6               −21.3           −1.00
            AT/TA                      −7.2               −20.4           −0.88
            TA/AT                      −7.2               −21.3           −0.58
            CA/GT                      −8.5               −22.7           −1.45
            GT/CA                      −8.4               −22.4           −1.44
            CT/GA                      −7.8               −21.0           −1.28
            GA/CT                      −8.2               −22.2           −1.30
            CG/GC                     −10.6               −27.2           −2.17
            GC/CG                      −9.8               −24.4           −2.24
            GG/CC                      −8.0               −19.9           −1.84

            Initiation                 +0.2                −5.7           +1.96
            Symmetry correction         0.0                −1.4           +0.43
            Terminal AT penalty        +2.2                +6.9           +0.05

        taken from SantaLucia, Hicks (2004)

        Parameters
        ----------
        S1: str
            the first strand
        S2: str
            the second strand
        T: float
            the temperature in Kelvin

        Returns
        -------
        float
            the Gibbs Free Energy of binding

    """

    D_G = 0

    # G_initiation
    D_G += INIT[0] - ((T * INIT[1]) / 1000)

    # G_symmetry
    if is_self_complementary(S1):
        D_G += SYMC[0] - ((T * SYMC[1]) / 1000)

    # G_stack
    for i in range(len(S1) - 1):
        seq1 = S1[i:i + 2]
        seq2 = S2[i:i + 2]

        if is_wc_pair(seq1, seq2):
            D_G += calculate_wc_pair(seq1, seq2, T)
        else:
            D_G += calculate_mm_pair(seq1, seq2, T)

    # G_AT_terminal - start
    if (S1[0], S2[0]) in ATTA:
        D_G += TATP[0] - ((T * TATP[1]) / 1000)

    # G_AT_terminal - end
    if (S1[-1], S2[-1]) in ATTA:
        D_G += TATP[0] - ((T * TATP[1]) / 1000)

    return D_G






def is_wc_pair(seq1: str, seq2: str) -> bool:
    """

        checks to see if the two sequences are Watson-Crick pairs

        Parameters
        ----------
        seq1: str
            the first sequence
        seq2: str
            the second sequence

        Returns
        -------
        boolean
            true if the two sequences are Watson-Crick pairs, false otherwise

    """
    return (seq1, seq2) in WCDB


def calculate_wc_pair(seq1: str, seq2: str, T: float) -> float:
    """

        calculate the Energy of binding the Watson-Crick pair

        Parameters
        ----------
        seq1: str
            the first sequence
        seq2: str
            the second sequence
        T: float
            the temperature in Kelvin

        Returns
        -------
        float
            the Energy of binding the Watson-Crick pair

    """
    D_H, D_S = WCDB[(seq1, seq2)]
    return D_H - ((T * D_S) / 1000)


def calculate_mm_pair(seq1: str, seq2: str, T: float) -> float:
    """

        calculate the Energy of binding the mismatched pair

        Parameters
        ----------
        seq1: str
            the first sequence
        seq2: str
            the second sequence
        T: float
            the temperature in Kelvin

        Returns
        -------
        float
            the Energy of binding the mismatched pair

    """
    block1 = (seq1, seq2)

    if block1 in MMDB:
        return MMDB[block1]
    else:
        block2 = (seq2[::-1], seq1[::-1])

        if block2 in MMDB:
            return MMDB[block2]
        else:
            return 0

