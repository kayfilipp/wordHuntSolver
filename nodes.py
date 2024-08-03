from typing import Optional
from collections import defaultdict
from copy import deepcopy
"""
Contains classes related to the word search
"""

class Letter():
    """
    Represents a letter in the game's grid
    """
    character: str # a-z
    neighbors: list['Letter'] # all touching Letter objects
    coordinates: tuple[int, int] # (x, y)
    origin: Optional['Letter'] # the letter branched off of

    def __init__(self, character: str, coordinates: tuple[int, int]):
        self.character = character
        self.coordinates = coordinates
        self.neighbors = []
        self.currently_found = False # for recursion - can't make a word using same character twice

class SearchResults():
    """
    Holds all relevant data related to a game search
    NOTE: words_by_character likely includes less items than words_by_coordinates and words_found -
    can be multiple branches for spelling the same word
    """
    words_found: list[list[Letter]] # each inner list holds the subsequent Letter objects traversed needed to make a word
    longest_word: list[Letter] # the longest word that's been found
    words_by_character: set[str] # all words found in a search
    words_by_coordinates: list[list[tuple[int, int]]] # each inner list holds subsequent coordinates of letters that make up a word

    def __init__(self):
        self.words_found = []
        self.longest_word = []
        self.words_by_character = set()
        self.words_by_coordinates = []
    
    def find_data(self):
        """
        Uses the words_found attribute to find data for characters/coordinates
        """
        for word in self.words_found:
            self.words_by_coordinates.append([])
            new_word = []
            for letter in word:
                self.words_by_coordinates[-1].append(letter.coordinates)
                new_word.append(letter.character)
            self.words_by_character.add(''.join(new_word))

class Game():
    """
    Holds all relevant game info
    """

    prefixes: set # all possible prefixes 1-3 letters in english dictionary
    prefixes_to_words: dict[str, set[str]] # all 3 letter prefixes associated with a set of their words
    all_search_results: list[SearchResults] # contains all data related to each of the game's searches

    def __init__(self):
        self.create_hashes()
        self.all_search_results = []
        # connect ui commands to find_words() method
        # connect ui to find 2d_grid of characters for each search
    
    def find_words(self, character_2d_array: list[list[str]]):
        """
        Finds all possible words within the grid - using Search object's recursive_solver() method
        """
        results = SearchResults()
        new_search = Search(character_2d_array)
        for letter in new_search.letters_1d:
            new_search.recursive_solver(letter, results, first_call=True)

        results.find_data()
        self.all_search_results.append(results)
    
    def create_hashes(self):
        """
        Creates a hashset and a hashmap:
            - hashset contains all possible 1, 2, and 3 letter prefixes.
            - hashmap associates every possible 3 letter prefix with a set of its words
        
        'pre' is the 3-letter prefix with the largest number of words: 225

        hashset: {'a', 'ba', 'tor', ...}
        hashmap: {'tor': {'torn', 'torch', ...}, 'tra': {'train', 'trade', ...} ...}
        """
        prefixes = set()
        prefixes_to_words = defaultdict(set)
        
        with open('long_wordlist.txt') as f:
            for line in f:
                word = line.strip()
                # game only accepts 3 letter words
                if len(word) >= 3:
                    # adding prefix if not already existent
                    if word[0] not in prefixes:
                        prefixes.add(word[0])
                    if word[:2] not in prefixes:
                        prefixes.add(word[:2])
                    if word[:3] not in prefixes:
                        prefixes.add(word[:3])
                    
                    # adding all words to dictionary
                    prefixes_to_words[word[:3]].add(word)
    
        self.prefixes = prefixes
        self.prefixes_to_words = prefixes_to_words


class Search(Game):
    letters_2d: list[list[Letter]] # 2d array of game letters - first key is the column - second key is the row
    letters_1d: list[Letter] # 1d array of game letters
    length: int # length/width of grid
    current_word: str # the search branch's current word
    letters_traversed: list[Letter]
    
    def __init__(self, characters_2d: list[list[str]]):
        super().__init__()
        self.length = len(characters_2d)
        self.letters_2d = [[] for _ in range(self.length)] # to be populated
        self.set_letter_coordinates_and_characters(characters_2d)
        self.flatten_letters_2d()
        self.set_neighbors()
        self.current_word = ""
        self.letters_traversed = []

    def flatten_letters_2d(self):
        # looping through grid
        letters_1d = []
        for col in self.letters_2d:
            for letter in col:
                letters_1d.append(letter)

        self.letters_1d = letters_1d

    def set_letter_coordinates_and_characters(self, characters_2d):
        """
        Populates the letters_2d attribute with appropriate letter objects
        """
        for x in range(self.length):
            for y in range(self.length):
                character = characters_2d[x][y]
                self.letters_2d[x].append(Letter(character, (x, y)))

    def set_neighbors(self):
        """
        Attributes neighbors to every Letter object
        """
        # looping over columns
        for x, col in enumerate(self.letters_2d):
            # looping over rows
            for y, letter in enumerate(col):
                # adding neighbors if they exist
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        neighbor_coordinates = x+i, y+j
                        # skipping if the current neighbor is the letter itself
                        if i == 0 and j == 0:
                            pass
                        else:
                            # index out of range means letter is on an edge
                            if neighbor_coordinates[0] == -1 or neighbor_coordinates[0] == self.length \
                            or neighbor_coordinates[1] == -1 or neighbor_coordinates[1] == self.length:
                                pass
                            # index is valid and neighbor exists
                            else:
                                neighbor = self.letters_2d[neighbor_coordinates[0]][neighbor_coordinates[1]]
                                letter.neighbors.append(neighbor)

    def recursive_solver(self, current_letter: Letter, search_results: SearchResults, first_call=False):
        """
        Finds all possible words in the grid
        Possible words must be <= grid_length ** 2
        """
        # must reset tracking variables on initial call
        if first_call:
            self.current_word = current_letter.character
            self.letters_traversed = [current_letter]
            for letter in self.letters_1d:
                letter.currently_found = False
            current_letter.currently_found = True
        # word can't exceed the number of characters on the grid
        if len(self.current_word) == self.length ** 2:
            # could still be a valid word, though
            prefix = self.current_word[:3]
            if self.current_word in self.prefixes_to_words[prefix]:
                    search_results.words_found.append(deepcopy(self.letters_traversed))
                    # checking if its the longest word added
                    if len(self.letters_traversed) > len(search_results.longest_word):
                        search_results.longest_word = deepcopy(self.letters_traversed)
            return
        
        
        possible_next_letters = [letter for letter in current_letter.neighbors if not letter.currently_found]

        for neighbor in possible_next_letters:
            prefix_length = len(self.current_word)
            # checking if start of the word is a possible prefix
            if prefix_length <= 3:
                if self.current_word not in self.prefixes:
                    return
                if prefix_length < 3:
                    # updating tracker variables
                    self.current_word += neighbor.character
                    self.letters_traversed.append(neighbor)
                    neighbor.currently_found = True
                    # finding new branch - only words with 3+ letters accepted
                    self.recursive_solver(neighbor, search_results)
            # current word has 3+ letters and has a valid prefix
            if prefix_length >= 3:
                # checking if the current word is an actual word
                prefix = self.current_word[:3]
                if self.current_word in self.prefixes_to_words[prefix]:
                    search_results.words_found.append(deepcopy(self.letters_traversed))
                    # checking if its the longest word added
                    if len(self.letters_traversed) > len(search_results.longest_word):
                        search_results.longest_word = deepcopy(self.letters_traversed)
                # checking if the current word + neighbor's character is a possible word
                possible_big_prefix = self.current_word + neighbor.character # prefix containing 4+ characters
                # possible words must start with the current prefix
                possible_words = [word for word in self.prefixes_to_words[prefix] \
                                  if len(word) >= len(possible_big_prefix) and word[:len(possible_big_prefix)] == possible_big_prefix]
                if len(possible_words) == 0: # base case - branch is done
                    return
                # more possible words to go
                else:
                    # updating tracker variables
                    self.current_word = possible_big_prefix
                    self.letters_traversed.append(neighbor)
                    neighbor.currently_found = True
                    # starting new branch
                    self.recursive_solver(neighbor, search_results)
            
            # after this stage of the branch has fully been searched, tracker variables are cut/reset
            self.current_word = self.current_word[:-1]
            prev_letter = self.letters_traversed.pop()
            prev_letter.currently_found = False