
from utils.dna import self_complementary


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

ATTA = {"AT", "TA"}

INIT = (0.2, -5.7)
TATP = (2.2,  6.9)
SYMC = (0,   -1.4)

'''

    AA/TT                  −7.6    −21.3    −1.00
    AT/TA                  −7.2    −20.4    −0.88
    TA/AT                  −7.2    −21.3    −0.58
    CA/GT                  −8.5    −22.7    −1.45
    GT/CA                  −8.4    −22.4    −1.44
    CT/GA                  −7.8    −21.0    −1.28
    GA/CT                  −8.2    −22.2    −1.30
    CG/GC                 −10.6    −27.2    −2.17
    GC/CG                  −9.8    −24.4    −2.24
    GG/CC                  −8.0    −19.9    −1.84

    Initiation             +0.2     −5.7    +1.96

    Terminal AT penalty    +2.2     +6.9    +0.05

    Symmetry correction     0.0     −1.4    +0.43

'''
def free_energy(S1: str, S2: str, T: float) -> float:
    G = 0

    G += INIT[0] - ((T * INIT[1]) / 1000)

    if self_complementary(S1):
        G += SYMC[0] - ((T * SYMC[1]) / 1000)

    for i in range(len(S1) - 1):
        H, S = TDB[f"{S1[i:i + 2]}/{S2[i:i + 2]}"]
        G += H - ((T * S) / 1000)

    if f"{S1[0]}{S2[0]}" in ATTA:
        G += TATP[0] - ((T * TATP[1]) / 1000)

    if f"{S1[-1]}{S2[-1]}" in ATTA:
        G += TATP[0] - ((T * TATP[1]) / 1000)

    return G
