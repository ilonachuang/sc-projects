"""
File: boggle.py
Name: Ilona
----------------------------------------
TODO: This program asks for 4 rows * 4 characters of the alphabet to set up a boggle game,
	and the program will tell how many words there are in total.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# Global Variable
dictionary = {}


def main():
	"""
	TODO: This program asks for 4 rows * 4 characters of the alphabet to set up a boggle game,
		and the program will tell how many words there are in total.
	"""
	count = [0]		# to keep track of the amount of words
	words = []		# to store the words
	read_dictionary()	 # set dictionary
	letters = ask_for_input()  # set boggle board
	start = time.time()
	if letters is not None:		# all the inputs are correct
		# 16 recursions in total, starting from letters[0][0]
		for i in range(4):
			for j in range(4):
				search_boggle(i, j, letters, letters[i][j], count, [(i, j)], words)
		print(f'There are {count[0]} words in total.')

		end = time.time()
		print('----------------------------------')
		print(f'The speed of your boggle algorithm: {end - start} seconds.')


def search_boggle(index1, index2, letters, current_s, count, index_lst, words):
	"""
	:param index1: int, current row
	:param index2: int, current index in current row
	:param letters: list, the boggle board
	:param current_s: str, the current string to form an existing word
	:param count: list, count[0] keeps track of the amount of words
	:param index_lst: list, the list that stores used (row, index)
	:param words: list, the list that stores existing words
	"""
	if len(current_s) >= 4 and current_s not in words and current_s in dictionary[current_s[0]]:
		words.append(current_s)
		print(f'Found "{current_s}"')
		count[0] += 1
		# keep checking if there are more possibilities
		search_boggle(index1, index2, letters, current_s, count, index_lst, words)
	else:
		for i in range(-1, 2, 1):		# i = -1, 0, 1
			for j in range(-1, 2, 1):	 # j = -1, 0, 1
				new_index1 = index1+i
				new_index2 = index2+j
				if 0 <= new_index1 <= 3 and 0 <= new_index2 <= 3:
					if (new_index1, new_index2) not in index_lst:	 # not used before
						neighbor = letters[new_index1][new_index2]
						# Choose
						current_s += neighbor
						index_lst.append((new_index1, new_index2))
						if has_prefix(current_s):
							# Explore
							search_boggle(new_index1, new_index2, letters, current_s, count, index_lst, words)
						# Un-choose
						current_s = current_s[:-1]
						index_lst.pop()


def ask_for_input():
	"""
	This function asks for 4 rows of input, and checks the input a row at a time
	:return: list, the boggle board
	"""
	letters = []  # create boggle board
	for i in range(4):
		row = input(f'{i+1} row of letters: ').lower().split()	 # case insensitive
		if correct_input(row):
			letters.append(row)
		else:
			break
	if len(letters) == 4:
		return letters


def correct_input(row):
	"""
	:param row: str, user input
	:return: bool, if the user input is correct
	"""
	for i in range(len(row)):
		if len(row[i]) != 1 or len(row) != 4:
			print('Illegal input')
			return False
	return True


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		for line in f:
			if line[0] in dictionary:
				dictionary[line[0]].append(line[:-1])
			else:
				dictionary[line[0]] = [line[:-1]]


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dictionary[sub_s[0]]:
		if word.startswith(sub_s):
			return True


if __name__ == '__main__':
	main()
