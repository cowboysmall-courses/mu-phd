
from sdc.tile import Tile
from sdc import *

from utils.dna import is_self_complementary

import math


TDB = {
    "AA/TT":  (-7.6, -21.3), "TT/AA":  (-7.6, -21.3),
    "AT/TA":  (-7.2, -20.4), "TA/AT":  (-7.2, -21.3),
    "CA/GT":  (-8.5, -22.7), "TG/AC":  (-8.5, -22.7),
    "GT/CA":  (-8.4, -22.4), "AC/TG":  (-8.4, -22.4),
    "CT/GA":  (-7.8, -21.0), "AG/TC":  (-7.8, -21.0),
    "GA/CT":  (-8.2, -22.2), "TC/AG":  (-8.2, -22.2),
    "CG/GC": (-10.6, -27.2), "GC/CG":  (-9.8, -24.4),
    "GG/CC":  (-8.0, -19.9), "CC/GG":  (-8.0, -19.9)
}

# MMDB = {
#     "CT/GG": -0.32,
#     "GG/CG": -1.11,
#     "GC/GA":  0.47,
#     "TG/GC": -0.47,
#     "CT/AC": -0.47
# }

ATTA = {"AT", "TA"}

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
    return k_f * math.exp( (gibbs_rl(left, tile, T) + gibbs_m(tile, T) + gibbs_rl(tile, right, T)) / (k_B * T) )



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
    return free_energy(tile_left.right(), tile_right.left()[::-1], T)


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
    return free_energy(tile.middle(), tile.middle_c(), T)


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
        block = f"{S1[i:i + 2]}/{S2[i:i + 2]}"

        if block in TDB:
            D_H, D_S = TDB[block]
            D_G += D_H - ((T * D_S) / 1000)
        #
        # G_mismatch - fix this!!!
        #
        # else:
        #     D_G += MMDB[block]


    # G_AT_terminal - start
    if f"{S1[0]}{S2[0]}" in ATTA:
        D_G += TATP[0] - ((T * TATP[1]) / 1000)

    # G_AT_terminal - end
    if f"{S1[-1]}{S2[-1]}" in ATTA:
        D_G += TATP[0] - ((T * TATP[1]) / 1000)

    return D_G
