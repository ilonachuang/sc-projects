"""
File: anagram.py
Name: Ilona
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global Variable
dictionary = {}


def main():
    """
    TODO: This program recursively finds all anagrams of the inputted alphabets
    """
    print('Welcome to stanCode \"Anagram Generator\" (or -1 to quit)')
    read_dictionary()   # set dictionary
    while True:
        find = input('Find anagrams for: ')
        start = time.time()
        if find == EXIT:
            break
        else:
            print('Searching...')
            anagram_lst = find_anagrams(find)   # all anagrams
            print(f'{len(anagram_lst)} anagrams:', anagram_lst)
            end = time.time()
            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    with open(FILE, 'r') as f:
        for line in f:
            if line[0] in dictionary:
                dictionary[line[0]].append(line[:-1])
            else:
                dictionary[line[0]] = [line[:-1]]


def find_anagrams(s):
    """
    :param s: str, the inputted alphabets
    :return: list, anagram list
    """
    current_lst = []
    d = {}
    # this dictionary keeps track of the amount of each alphabet inputted and used
    for ch in s:
        if ch not in d:
            d[ch] = 1
        else:
            d[ch] += 1
    find_anagrams_helper(s, '', current_lst, d)
    return current_lst


def find_anagrams_helper(s, current_s, current_lst, s_dict):
    """
    :param s: str, the inputted alphabets
    :param current_s: str, the current string to form an anagram
    :param current_lst: list, the current list storing anagrams
    :param s_dict:  str, the dictionary keeping track of the amount of each alphabet inputted and used
    """
    if len(current_s) == len(s) and current_s not in current_lst and current_s in dictionary[current_s[0]]:
        print(current_s)
        print('Searching...')
        current_lst.append(current_s)
    else:
        for ch in s:
            if s_dict[ch] != 0:    # there are characters left
                # Choose
                current_s += ch
                s_dict[ch] -= 1
                if len(current_s) == 1 or has_prefix(current_s):
                    # Explore
                    find_anagrams_helper(s, current_s, current_lst, s_dict)     # recursion
                # Un-choose
                current_s = current_s[:len(current_s)-1]
                s_dict[ch] += 1


def has_prefix(sub_s):
    """
    :param sub_s: string, the substring for word check
    :return: bool, if there is a word in dictionary that starts with substring
    """
    for word in dictionary[sub_s[0]]:
        if word.startswith(sub_s):
            return True


if __name__ == '__main__':
    main()
