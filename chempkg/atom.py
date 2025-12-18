"""
Module définissant la classe Atom et l'ensemble du tableau périodique.
Les données proviennent des standards IUPAC et de la documentation fournie.
"""
from typing import Tuple, Dict

def get_elec_config(num_electron: int) -> Tuple[str, ...]:
    """
    Génère la configuration électronique selon la règle de Klechkowski.
    Ordre: 1s -> 2s ... -> 7p
    """
    orbital_order = [
        (1, 's', 2), (2, 's', 2), (2, 'p', 6), (3, 's', 2), (3, 'p', 6),
        (4, 's', 2), (3, 'd', 10), (4, 'p', 6), (5, 's', 2), (4, 'd', 10),
        (5, 'p', 6), (6, 's', 2), (4, 'f', 14), (5, 'd', 10), (6, 'p', 6),
        (7, 's', 2), (5, 'f', 14), (6, 'd', 10), (7, 'p', 6)
    ]

    config = []
    electrons_restants = num_electron

    for n, orbital_type, capacity in orbital_order:
        if electrons_restants <= 0:
            break

        nb_in_orbital = min(electrons_restants, capacity)
        config.append(f"{n}{orbital_type}{nb_in_orbital}")
        electrons_restants -= nb_in_orbital

    return tuple(config)


class Atom:
    """
    Représente un atome chimique défini par son symbole, numéro atomique et masse.
    """
    def __init__(self, name: str, num_electron: int, weight: float):
        self.name = name
        self.num_electron = num_electron
        self.weight = float(weight)
        # La configuration est calculée automatiquement à l'instanciation
        self.elec_config = get_elec_config(num_electron)

    def __repr__(self) -> str:
        # Format strict requis par les tests unitaires
        return f'Atom(name="{self.name}", num_electron={self.num_electron}, weight={self.weight})'

    def __str__(self) -> str:
        return f"{self.name} ({self.weight}, {self.num_electron})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Atom):
            return NotImplemented
        return (self.name == other.name and
                self.num_electron == other.num_electron and
                self.weight == other.weight)

    def __hash__(self):
        return hash((self.name, self.num_electron, self.weight))


# --- DONNÉES ET GÉNÉRATION DYNAMIQUE ---

# Dictionnaire qui servira de registre pour mol.py
ATOM_REGISTRY: Dict[str, Atom] = {}

def _initialize_periodic_table():
    """
    Fonction privée pour peupler l'espace de noms global et le registre.
    """
    # Format: (Symbole, Z, Masse)
    periodic_data = [
        ("H", 1, 1.0), ("He", 2, 4.0), ("Li", 3, 6.94), ("Be", 4, 9.01),
        ("B", 5, 10.81), ("C", 6, 12.0), ("N", 7, 14.0), ("O", 8, 16.0),
        ("F", 9, 19.0), ("Ne", 10, 20.18), ("Na", 11, 23.0), ("Mg", 12, 24.3),
        ("Al", 13, 26.98), ("Si", 14, 28.09), ("P", 15, 31.0), ("S", 16, 32.0),
        ("Cl", 17, 35.5), ("Ar", 18, 39.95), ("K", 19, 39.0), ("Ca", 20, 40.0),
        ("Sc", 21, 44.96), ("Ti", 22, 47.87), ("V", 23, 50.94), ("Cr", 24, 52.0),
        ("Mn", 25, 54.94), ("Fe", 26, 56.0), ("Co", 27, 59.0), ("Ni", 28, 58.69),
        ("Cu", 29, 63.55), ("Zn", 30, 65.0), ("Ga", 31, 69.72), ("Ge", 32, 72.63),
        ("As", 33, 74.92), ("Se", 34, 78.96), ("Br", 35, 79.9), ("Kr", 36, 83.79),
        ("Rb", 37, 85.47), ("Sr", 38, 87.62), ("Y", 39, 88.91), ("Zr", 40, 91.22),
        ("Nb", 41, 92.91), ("Mo", 42, 96.0), ("Tc", 43, 98.0), ("Ru", 44, 101.07),
        ("Rh", 45, 102.91), ("Pd", 46, 106.42), ("Ag", 47, 107.87), ("Cd", 48, 112.41),
        ("In", 49, 114.82), ("Sn", 50, 118.71), ("Sb", 51, 121.76), ("Te", 52, 127.6),
        ("I", 53, 127.0), ("Xe", 54, 131.29), ("Cs", 55, 132.91), ("Ba", 56, 137.33),
        ("La", 57, 138.91), ("Ce", 58, 140.12), ("Pr", 59, 140.91), ("Nd", 60, 144.24),
        ("Pm", 61, 145.0), ("Sm", 62, 150.36), ("Eu", 63, 151.96), ("Gd", 64, 157.25),
        ("Tb", 65, 158.93), ("Dy", 66, 162.5), ("Ho", 67, 164.93), ("Er", 68, 167.3),
        ("Tm", 69, 168.93), ("Yb", 70, 173.05), ("Lu", 71, 174.97), ("Hf", 72, 178.49),
        ("Ta", 73, 180.95), ("W", 74, 183.84), ("Re", 75, 186.21), ("Os", 76, 190.23),
        ("Ir", 77, 192.22), ("Pt", 78, 195.08), ("Au", 79, 197.0), ("Hg", 80, 200.59),
        ("Tl", 81, 204.38), ("Pb", 82, 207.2), ("Bi", 83, 208.98), ("Po", 84, 209.0),
        ("At", 85, 210.0), ("Rn", 86, 222.0), ("Fr", 87, 223.0), ("Ra", 88, 226.0),
        ("Ac", 89, 227.0), ("Th", 90, 232.04), ("Pa", 91, 231.04), ("U", 92, 238.03),
        ("Np", 93, 237.0), ("Pu", 94, 244.0), ("Am", 95, 243.0), ("Cm", 96, 247.0),
        ("Bk", 97, 247.0), ("Cf", 98, 251.0), ("Es", 99, 252.0), ("Fm", 100, 257.0),
        ("Md", 101, 258.0), ("No", 102, 259.0), ("Lr", 103, 262.0), ("Rf", 104, 267.0),
        ("Db", 105, 268.0), ("Sg", 106, 271.0), ("Bh", 107, 272.0), ("Hs", 108, 270.0),
        ("Mt", 109, 276.0), ("Ds", 110, 281.0), ("Rg", 111, 280.0), ("Cn", 112, 285.0),
        ("Nh", 113, 284.0), ("Fl", 114, 289.0), ("Mc", 115, 288.0), ("Lv", 116, 293.0),
        ("Ts", 117, 294.0), ("Og", 118, 294.0)
    ]

    for symbol, z, weight in periodic_data:
        atom_instance = Atom(symbol, z, weight)
        ATOM_REGISTRY[symbol] = atom_instance
        # Injection dans l'espace global du module pour les imports
        globals()[symbol] = atom_instance

# Exécution immédiate
_initialize_periodic_table()
