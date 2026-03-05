from bfajps import knapsack_problem
import itertools

def test_knapsack_problem():
    assert knapsack_problem([10, 6, 8, 7, 9], [5, 9, 6, 3, 9], 16, 10) == (0, 0, 0, 1, 1)
    assert knapsack_problem([10, 6, 7, 9], [5, 6, 3, 9], 10, 8) == (0, 0, 0, 1)
    assert knapsack_problem([10, 6, 7, 9], [5, 6, 3, 9], 5, 300) == False
    assert knapsack_problem([2, 4], [3, 5], 6, 80) == False