import os
from pathlib import Path

import numpy as np

from chempkg.mol import Molecule
from chempkg.reaction_utils import valid_reaction, kinetic_decomp

reactions = [
    # Balanced: 2 H2 + O2 → 2 H2O
    (([(Molecule("H2"), 2), (Molecule("O2"), 1)], [(Molecule("H2O"), 2)]), True),

    # Unbalanced: H2 + O2 → H2O
    (([(Molecule("H2"), 1), (Molecule("O2"), 1)], [(Molecule("H2O"), 1)]), False),

    # Balanced: CH4 + 2 O2 → CO2 + 2 H2O
    (([(Molecule("CH4"), 1), (Molecule("O2"), 2)], [(Molecule("CO2"), 1), (Molecule("H2O"), 2)]), True),

    # Unbalanced: CH4 + O2 → CO2 + H2O
    (([(Molecule("CH4"), 1), (Molecule("O2"), 1)], [(Molecule("CO2"), 1), (Molecule("H2O"), 1)]), False),

    # 2 Na + Cl2 → 2 NaCl
    (([(Molecule("Na"), 2), (Molecule("Cl2"), 1)], [(Molecule("NaCl"), 2)]), True),

    # C3H8 + 5 O2 → 3 CO2 + 4 H2O
    (([(Molecule("C3H8"), 1), (Molecule("O2"), 5)], [(Molecule("CO2"), 3), (Molecule("H2O"), 4)]), True),

    # 2 KClO3 → 2 KCl + 3 O2
    (([(Molecule("KClO3"), 2)], [(Molecule("KCl"), 2), (Molecule("O2"), 3)]), True),

    # 2 C8H18 + 25 O2 → 16 CO2 + 18 H2O
    (([(Molecule("C8H18"), 2), (Molecule("O2"), 25)], [(Molecule("CO2"), 16), (Molecule("H2O"), 18)]), True),

    # 2 HCl + Na2CO3 → 2 NaCl + H2O + CO2
    (([(Molecule("HCl"), 2), (Molecule("Na2CO3"), 1)], [(Molecule("NaCl"), 2), (Molecule("H2O"), 1), (Molecule("CO2"), 1)]), True),
]

def test_valid_reaction():

    for (reactives, products), expected in reactions:
        result = valid_reaction(reactives=reactives, products=products)
        assert result == expected


kinetic_params = [
    ((0.1, 0.5, 5, 10), [0.01430667, 0.0108368,  0.0082085]),
    ((0.1, 0.5, 5, 25), [0.01010978, 0.00910967, 0.0082085]),
]

def test_kinetic_decomp():
    for (A0, k, T, steps), expected in kinetic_params:
        A_t = kinetic_decomp(A0, k, T, steps)

        assert len(A_t) == steps
        assert all(np.isclose(A_t[-3:], np.array(expected)))


def test_figure_plot():
    HERE = Path(__file__).parent
    _ = kinetic_decomp(0.1, 0.5, 5, 10, HERE / "test.png")
    assert os.path.isfile(HERE / "test.png")
    os.remove(HERE / "test.png")

