import itertools

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