"""
Module utilitaire pour gérer les réactions chimiques et la cinétique.
"""
from typing import List, Tuple, Optional
import numpy as np
import matplotlib.pyplot as plt
from .mol import Molecule

def valid_reaction(reactives: List[Tuple[Molecule, int]],
                   products: List[Tuple[Molecule, int]]) -> bool:
    """
    Vérifie si une réaction chimique est équilibrée.
    """
    def count_total_atoms(molecules_list):
        total_atoms = {}
        for mol, coeff in molecules_list:
            for atom, atom_count in mol.atoms.items():
                if atom not in total_atoms:
                    total_atoms[atom] = 0
                total_atoms[atom] += atom_count * coeff
        return total_atoms

    atoms_reactives = count_total_atoms(reactives)
    atoms_products = count_total_atoms(products)

    return atoms_reactives == atoms_products


def kinetic_decomp(A0: float, k: float, T: float, steps: int = 10,
                   figure_path: Optional[str] = None) -> np.ndarray:
    # pylint: disable=invalid-name
    """
    Modélise la cinétique d'une réaction de décomposition d'ordre 1.
    [A](t) = A0 * exp(-k * t)
    Arguments A0 et T conservés pour respecter la nomenclature du sujet.
    """
    # Création du vecteur temps avec numpy
    time_array = np.linspace(0, T, steps)

    # Calcul vectoriel
    concentration_array = A0 * np.exp(-k * time_array)

    if figure_path:
        # Création de la figure
        plt.figure(figsize=(8, 6))
        plt.plot(time_array, concentration_array, label="[A](t)")
        plt.title("Evolution de [A](t)")
        plt.xlabel("temps (en secondes)")
        plt.ylabel("[A](t) en mol.L-1")
        plt.legend()
        plt.grid(True)

        # Sauvegarde
        plt.savefig(figure_path)
        plt.close() # Important pour ne pas garder la figure en mémoire

    return concentration_array
