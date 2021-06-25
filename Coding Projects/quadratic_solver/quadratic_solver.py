"""
File: quadratic_solver.py
Name: Ilona Chuang
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	This program asks user a, b, and c for equation:
	ax^2 + bx + c = 0
	Then it checks if there are 0, 1, or 2 roots to this equation
	and shows the root(s) in the console.
	If there are no roots, console shows "No real roots."
	"""
	print('stanCode Quadratic Solver! ')					# introduction
	a = int(input('Enter a: '))
	b = int(input('Enter b: '))
	c = int(input('Enter c: '))
	disc = b*b - 4*a*c										# discriminant to determine roots
	if disc < 0:
		print('No real roots')								# disc < 0, do not proceed to calculate
	elif disc == 0:											# disc == 0, one root
		ans = -b/(2*a)
		print('One root: ' + str(ans))
	else:													# disc > 0, calculate two roots
		ans1 = (-b + math.sqrt(disc))/(2 * a)
		ans2 = (-b - math.sqrt(disc))/(2 * a)
		print('Two roots: ' + str(ans1) + ', ' + str(ans2))




###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
