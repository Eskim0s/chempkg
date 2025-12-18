"""
Module définissant la classe Molecule.
"""
import re
from typing import Dict
from .atom import Atom, ATOM_REGISTRY

class Molecule:
    """
    Représente une molécule composée d'atomes.
    """
    def __init__(self, formula: str):
        self.formula = formula
        self.atoms: Dict[Atom, int] = self._parse_formula(formula)
        self.weight: float = self._calculate_weight()

    def _parse_formula(self, formula: str) -> Dict[Atom, int]:
        """
        Convertit une string (ex: 'CH3COOH') en dictionnaire d'atomes.
        Gère les atomes répétés dans la formule.
        """
        atoms_dict = {}
        # Regex: Majuscule + (minuscule optionnelle) + (nombre optionnel)
        pattern = re.compile(r"([A-Z][a-z]?)(\d*)")

        # findall renvoie une liste de tuples [('C', ''), ('H', '3'), ('C', ''), ...]
        matches = pattern.findall(formula)

        # Vérification qu'on a bien parsé toute la chaine
        parsed_length = sum(len(sym) + len(nb) for sym, nb in matches)
        if parsed_length != len(formula):
            pass

        for symbol, count_str in matches:
            if symbol not in ATOM_REGISTRY:
                raise ValueError(f"Atome inconnu: {symbol}")

            atom_obj = ATOM_REGISTRY[symbol]
            count = int(count_str) if count_str else 1

            # Accumulation (ex: C... C... -> total C)
            if atom_obj in atoms_dict:
                atoms_dict[atom_obj] += count
            else:
                atoms_dict[atom_obj] = count

        return atoms_dict

    def _calculate_weight(self) -> float:
        """Calcule la masse totale de la molécule."""
        total_weight = 0.0
        for atom, count in self.atoms.items():
            total_weight += atom.weight * count
        return total_weight

    def __repr__(self) -> str:
        return f'Molecule("{self.formula}")'

    def __str__(self) -> str:
        return f"Molecule {self.formula} (Weight: {self.weight})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Molecule):
            return NotImplemented
        return self.atoms == other.atoms
