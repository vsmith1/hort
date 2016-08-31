# hort.py
# Program to flip a coin

import random

flipCount = int(input("How many flips?"))

while (flipCount > 0):
	flip = random.randint (0,1)
	if flip == 0:
		flipWord = "heads"
	else:
		flipWord = "tails"
	print ("I flipped a coin and got ",flipWord,".")
	flipCount -= 1
