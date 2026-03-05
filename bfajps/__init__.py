import itertools
import networkx as nx

# programa para ver si es h

def is_hamiltonian_cycle(graph, cycle):
    """Checks if cycle is a hamiltonian cycle in graph.
    Graph is a Networkx graph, and cycle is a list of vertices"""
    n = len(set(cycle))
    if n != graph.order():
        return False
    for i in range(n-1):
        if not graph.has_edge(cycle[i], cycle[i+1]):
            return False
    if not graph.has_edge(cycle[n-1], cycle[0]):
        return False
    return True

def is_hamiltonian(graph):
    vertices = list(graph.nodes())
    if len(vertices) < 3:
        return False
    perms = itertools.permutations(vertices)
    for perm in perms:
        if is_hamiltonian_cycle(graph, perm):
            return perm
    return False

# programa de los colores

def is_proper_coloring(graph, coloring):
    for edge in graph.edges():
        if coloring[edge[0]] == coloring[edge[1]]:
            return False
    return True

def is_3_coloring(graph):
    n = graph.order()
    colorings = itertools.product([0,1,2], repeat = n)
    for coloring in colorings:
        if is_proper_coloring(graph, coloring):
            return coloring
    return False

# programa de peso en la mochila

def sum_of_vaules(weihts, key):
    # Calculate the total value based on weights and a selection key
    weiht_total=0
    for i in range(len(weihts)):
        weiht_total += weihts[i]*key[i]
    return weiht_total

def knapsack_problem(weihts, profits, capacity, goal):
    # Get the number of items
    n = len(profits)
    # Generate all possible combinations of selecting items (0 for not selected, 1 for selected)
    sequences = itertools.product([0,1], repeat = n)
    # Iterate through each combination
    for sequence in sequences:
        # Check if the total weight of the selected items is within capacity
        # and if the total profit meets or exceeds the goal
        if sum_of_vaules(weihts, sequence) <= capacity \
        and sum_of_vaules(profits, sequence) >= goal:
                # If both conditions are met, return the sequence of selected items
                return sequence
    # If no sequence satisfies the conditions, return False
    return False