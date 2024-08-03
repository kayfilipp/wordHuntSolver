import pytest
from classes import Nodes as nodes


def test_Search_constructor():
    new_search = nodes.Search([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']])
    for letter in new_search.letters_1d: # type: ignore
        list_of_neighbor_chars = [neighbor.character for neighbor in letter.neighbors]
        ... # checked with integrated debugger

def test_recursive_solver_2():
    new_game = nodes.Game()
    grid = [['c', 'a'], ['o', 't']]
    new_game.find_words(grid)
    ... # checked with integrated debugger

def test_recursive_solver_3():
    new_game = nodes.Game()
    grid = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
    new_game.find_words(grid)
    ... # checked with integrated debugger

def test_recursive_solver_3_again():
    new_game = nodes.Game()
    grid = [['a', 'c', 'c'], ['p', 'r', 'e'], ['d', 'e', 'd']]
    new_game.find_words(grid)
    ... # checked with integrated debugger

def test_recursive_solver_4():
    new_game = nodes.Game()
    grid = [['a', 'c', 'c', 'f'], ['h', 'j', 'j', 'j'], ['e', 'w', 'w', 'w'], ['i', 'o', 'o', 'j']]
    new_game.find_words(grid)
    ... # checked with integrated debugger

def test_recursive_solver_5():
    new_game = nodes.Game()
    grid = [['a', 'b', 'c', 'd', 'e'], ['b', 'c', 'd', 'e', 'f'], ['c', 'd', 'e', 'f', 'g'], ['d', 'e', 'f', 'g', 'h'], ['e', 'f', 'g', 'h', 'i']]
    new_game.find_words(grid)
    ... # checked with integrated debugger

if __name__ == '__main__':
    pytest.main(['test_nodes.py'])