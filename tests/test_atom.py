from chempkg.atom import Atom

ATOMS =[
    (("O", 8, 16), ('1s2', '2s2', '2p4')),
    (("C", 6, 12), ('1s2', '2s2', '2p2')),
    (("H", 1, 1), ('1s1',)),
    (("P", 15, 31), ('1s2', '2s2', '2p6', '3s2', '3p3')),
    (("K", 19, 39), ('1s2', '2s2', '2p6', '3s2', '3p6', '4s1')),
    (("Na", 11, 23), ('1s2', '2s2', '2p6', '3s1')),
    (("Cl", 17, 35.5,), ('1s2', '2s2', '2p6', '3s2', '3p5')),
    (("Mg", 12, 24.3,), ('1s2', '2s2', '2p6', '3s2')),
    (("Fe", 26, 55.8,), ('1s2', '2s2', '2p6', '3s2', '3p6', '4s2', '3d6')),
    (("Zn", 30, 65,), ('1s2', '2s2', '2p6', '3s2', '3p6', '4s2', '3d10')),
    (("Au", 79, 197.,), ('1s2', '2s2', '2p6', '3s2', '3p6', '4s2', '3d10', '4p6', '5s2', '4d10', '5p6', '6s2', '4f14', '5d9')),
    (("Fl", 114, 289.,), ('1s2', '2s2', '2p6', '3s2', '3p6', '4s2', '3d10', '4p6', '5s2', '4d10', '5p6', '6s2', '4f14', '5d10', '6p6', '7s2', '5f14', '6d10', '7p2')),
    (("Er", 68, 167.3,), ('1s2', '2s2', '2p6', '3s2', '3p6', '4s2', '3d10', '4p6', '5s2', '4d10', '5p6', '6s2', '4f12')),
    (("Er", 87, 223.,), ('1s2', '2s2', '2p6', '3s2', '3p6', '4s2', '3d10', '4p6', '5s2', '4d10', '5p6', '6s2', '4f14', '5d10', '6p6', '7s1')),
]

def test_atom_base_attributes():
    for (name, num_electron, weight), _ in ATOMS:
        at = Atom(name=name, weight=weight, num_electron=num_electron)
        # assert the basic attributes are well defined
        assert at.name == name
        assert at.num_electron == num_electron
        assert at.weight == weight

def test_atom_elec_config():
    for (name, num_electron, weight), elec_config in ATOMS:
        at = Atom(name=name, weight=weight, num_electron=num_electron)
        # test if the elec_config is as expected
        assert at.elec_config == elec_config

def test_atom_methods():
    atoms = []

    for (name, num_electron, weight), _ in ATOMS:
        at = Atom(name=name, weight=weight, num_electron=num_electron)
        # assert that the objects have __repr__ and __str__ methods
        assert hasattr(at, "__repr__")
        assert hasattr(at, "__str__")

        # check if the str form of atom is as expected
        for t in (name, num_electron, weight):
            assert str(t) in str(at)

        atoms.append(at)

    # test the eq method
    assert atoms[0] == atoms[0]
    assert atoms[1] != atoms[0]

    

if __name__ == "__main__":
    test_atom_base_attributes()
    test_atom_elec_config()
    test_atom_methods()
