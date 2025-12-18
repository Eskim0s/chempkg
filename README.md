# Projet Chimie ISDS 2025 - Package chempkg

Ce projet implémente une librairie Python permettant de modéliser des structures chimiques (atomes, molécules) et de simuler des cinétiques de réaction, conformément aux exigences du cours de Python de l'ISUP et de Sorbonne Université pour le parcours SCDI du Master de Mathématiques et Applications.

## Installation

Le package est conçu pour être installable via pip.
Dans le dossier racine du projet, exécutez :

```bash
pip install .

```

Dépendances requises : numpy, matplotlib.

## Fonctionnalités

1. **Modélisation Atomique** : Gestion de tout le tableau périodique (H à Og) avec calcul automatique de la configuration électronique via la règle de Klechkowski .


2. **Modélisation Moléculaire** : Parsing intelligent de formules brutes (ex: "C2H5OH", "CH3COOH") et calcul de masse molaire .


3. **Cinétique Chimique** : Simulation vectorisée et visualisation graphique de réactions de décomposition d'ordre 1 .



## Exemples d'utilisation

Voici un script simple pour tester les fonctionnalités principales :

```python
from chempkg.atom import C, O, Fe
from chempkg.mol import Molecule
from chempkg.reaction_utils import kinetic_decomp

# 1. Propriétés atomiques
print(f"Atome : {Fe.name}, Masse : {Fe.weight}")
print(f"Configuration électronique du Carbone : {C.elec_config}")

# 2. Manipulation de molécules
ethanol = Molecule("C2H5OH")
print(f"Masse molaire de l'éthanol : {ethanol.weight} g/mol")

# 3. Simulation de cinétique
# Sauvegarde l'évolution de la concentration dans 'reaction.png'
concs = kinetic_decomp(A0=0.1, k=0.5, T=5.0, steps=10, figure_path="reaction.png")

```

## Tests et Qualité du Code

Ce projet met l'accent sur la fiabilité et la qualité du code, selon les standards du cours.

* **Tests Unitaires** : 11 tests validés couvrant toutes les fonctionnalités.
```bash
python -m pytest

```


* **Qualité du Code** : Code conforme PEP8, vérifié avec Pylint.


```bash
pylint chempkg

```



## Références

Les constantes et règles physiques implémentées se basent sur les standards scientifiques et les annexes du sujet :

* **Données atomiques** : [Wikipedia - Periodic Table](https://en.wikipedia.org/wiki/Periodic_table)
* **Règle de Klechkowski** : [Wikipedia - Electron Configuration.](https://en.wikipedia.org/wiki/Electron_configuration)
* **Conservation de la masse** : [Wikipedia - Molecule.](https://en.wikipedia.org/wiki/Molecule)
* **Atome** : [Wikipedia - Atom.](https://en.wikipedia.org/wiki/Atom)



## Auteur

Liam ADGH

Projet Python - ISUP 2025

Dépôt GitHub : https://github.com/Eskim0s/chempkg/

## Remerciements

Je tiens à remercier M. Etienne Guével (Ingénieur de Recherche - SCAI, etienne.guevel@sorbonne-universite.fr) pour la qualité de son enseignement, ses conseils sur les bonnes pratiques de développement et l'encadrement de ce projet.