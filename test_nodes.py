"""
PyTests for the Search(Game) class in Nodes.py

All resultant data is manually checked with VS code's integrated debugger -
done by setting breakpoints at ellipses (...)
"""

from time import time
import pytest
from classes import Nodes as nodes
from random import choice
import string

def test_Search_constructor():
    new_search = nodes.Search([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']])
    for letter in new_search.letters_1d: # type: ignore
        list_of_neighbor_chars = [neighbor.character for neighbor in letter.neighbors]
        ... # checked with integrated debugger - set breakpoint

def test_recursive_solver_1():
    new_game = nodes.Game()
    grid = [['a']]
    new_game.find_words(grid)
    ... # checked with integrated debugger - set breakpoint

def test_recursive_solver_2():
    new_game = nodes.Game()
    grid = [['c', 'a'], ['o', 't']]
    new_game.find_words(grid)
    ... # checked with integrated debugger - set breakpoint

def test_recursive_solver_3():
    new_game = nodes.Game()
    grid = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
    new_game.find_words(grid)
    ... # checked with integrated debugger - set breakpoint

def test_recursive_solver_3_again():
    new_game = nodes.Game()
    grid = [['a', 'c', 'c'], ['p', 'r', 'e'], ['d', 'e', 'd']]
    new_game.find_words(grid)
    ... # checked with integrated debugger - set breakpoint

def test_recursive_solver_4():
    new_game = nodes.Game()
    grid = [['a', 'c', 'c', 'f'], ['h', 'j', 'j', 'j'], ['e', 'w', 'w', 'w'], ['i', 'o', 'o', 'j']]
    new_game.find_words(grid)
    ... # checked with integrated debugger - set breakpoint

def test_recursive_solver_5():
    start_time = time()
    new_game = nodes.Game()
    grid = [['a', 'b', 'c', 'd', 'e'], ['b', 'c', 'd', 'e', 'f'], ['c', 'd', 'e', 'f', 'g'], ['d', 'e', 'f', 'g', 'h'], ['e', 'f', 'g', 'h', 'i']]
    new_game.find_words(grid)
    final_time = time()
    actual_completion_time = final_time - start_time
    ... # time/accuracy checked with integrated debugger - set breakpoint
    # ~0.85 seconds

def test_recursive_solver_10():
    start_time = time()
    new_game = nodes.Game()
    grid = [
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], # confusing - these are actually columns
            ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'], # so it should be flipped
            ['c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'],
            ['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'],
            ['e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'],
            ['f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'],
            ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'],
            ['h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q'],
            ['i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r'],
            ['j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's']
            ]
    new_game.find_words(grid)
    final_time = time()
    actual_completion_time = final_time - start_time
    ... # time/accuracy checked with integrated debugger - set breakpoint
    # ~6.4 seconds - not too shabby

def test_averages():
    new_game = nodes.Game()
    dimensions_to_avg_runtime = {}
    for dimensions in range(1, 11):
        for _ in range(100):
            new_game.find_words([[choice(string.ascii_lowercase) for _ in range(dimensions)] for _ in range(dimensions)])

        last_search_results = new_game.all_search_results[-100:]
        average_search_runtime = sum([search_result.search_time for search_result in last_search_results])/100
        dimensions_to_avg_runtime[dimensions] = round(average_search_runtime, 2)
    ... # runtime check

if __name__ == '__main__':
    pytest.main(['test_nodes.py'])