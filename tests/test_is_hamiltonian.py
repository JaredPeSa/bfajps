from bfajps import is_hamiltonian
import networkx as nx
atlas = nx.graph_atlas_g()
conexas = [g for g in atlas[1:] if nx.is_connected(g)]

def test_is_hamiltonian():
    assert is_hamiltonian(atlas[9]) == False
    assert is_hamiltonian(conexas[444]) == (0, 1, 6, 5, 4, 3, 2)