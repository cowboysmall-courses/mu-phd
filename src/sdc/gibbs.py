
from sdc.tile import NullTile, Tile
from sdc import k_f, R_j, u_0, WCDB, MMDB, ATTA, INIT, SYMC, TATP

from utils.dna import is_self_complementary

from typing import Callable

import math
import functools




def rate_attach(tile: Tile, concentration: int) -> float:
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
    # return k_f * tile.get_concentration()
    return k_f * concentration




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
    return k_f * math.exp( beta(T) * (gibbs_rl(left, tile, T) + gibbs_m(tile, T) + gibbs_rl(tile, right, T)) )



def beta(T: float) -> float:
    """

        calculate the value of Beta

        Parameters
        ----------
        T: float
            the temperature in Kelvin

        Returns
        -------
        float
            the value of Beta

    """
    return 1 / (R_j * T)




def mu(tile: Tile, T: float, concentration: int) -> float:
    """

        calculate the Chemical Potential of a tile

        Parameters
        ----------
        tile: Tile
            the provided tile
        T: float
            the temperature in Kelvin

        Returns
        -------
        float
            the Chemical Potential of a tile

    """
    # return (R_j * T) * math.log(tile.get_concentration() / u_0)
    return (R_j * T) * math.log(concentration / u_0)




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
    if isinstance(tile_left, NullTile) or isinstance(tile_right, NullTile):
        return 0
    return gibbs_free_energy(tile_left.get_right(), tile_right.get_left()[::-1], T)




def gibbs_rl_pa(l:Tile, r: Tile) -> Callable[[float], float]:
    """

        returns a function that calculates the Gibbs Free Energy of
        binding two compute domains of consecutive tiles - partial application

        Parameters
        ----------
        tile_left: Tile
            the first tile
        tile_right: Tile
            the second tile

        Returns
        -------
        Callable[[float], float]
            A function that calculates the Gibbs Free Energy of binding
            for a temperature T


    """
    @functools.cache
    def gibbs_rl_T(T: float) -> float:
        return gibbs_rl(l, r, T)
    return gibbs_rl_T




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
    if isinstance(tile, NullTile):
        return 0
    return gibbs_free_energy(tile.get_middle(), tile.get_middle_complement(), T)




def gibbs_m_pa(tile:Tile) -> Callable[[float], float]:
    """

        returns a function that calculates the Gibbs Free Energy of
        binding to a scaffold domains - partial application

        Parameters
        ----------
        tile: Tile
            the tile to bind to the scaffold

        Returns
        -------
        Callable[[float], float]
            A function that calculates the Gibbs Free Energy of binding
            for a temperature T

    """
    @functools.cache
    def gibbs_m_T(T: float) -> float:
        return gibbs_m(tile, T)
    return gibbs_m_T




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




def gibbs_free_energy(S1: str, S2: str, T: float) -> float:
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

