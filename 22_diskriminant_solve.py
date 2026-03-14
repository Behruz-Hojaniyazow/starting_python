import math
import numpy as np
from sympy import symbols, Eq, solve
def yechuvchi():
	print("--- Kwadrat tenglama yechuvchi ---")
	a = float(input("a-ni kiriting"))
	b = float(input("b-ni kiriting"))
	c = float(input("c-ni kiriting"))
	D = (b**2) - 4 * a * c
	print(f"\nDiskriminant: D={D}")
	if D >= 0:
		x1 = (-b + math.sqrt(D)) / (2 * a)
		x2 = (-b - math.sqrt(D)) / (2 * a)
		print(f"Tenglama javoblari: x1 = {x1}, x2 = {x2}")
	else:
		print("Tenglamaning javobi yoq chunki (D < 0)")
#Numpy usulida
	np_javob = np.roots([a, b, c])
	print(f"NumPy usulida: {np_javob}")
yechuvchi()