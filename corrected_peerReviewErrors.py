# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Cher M.
# Creation Date: September 22,2020
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()

def chooseCave():
	cave = '' ### Inconsistent use of tabs and spaces in indentation - spaces were used in this line, instead of tab
	while cave != '1' and cave != '2': ### Inconsistent use of tabs and spaces in indentation - spaces were used in this line, instead of tab
			print('Which cave will you go into? (1 or 2)') ### Inconsistent use of tabs and spaces in indentation - spaces were used in this line, instead of tab
			cave = input(cave)

	return cave ### "caves" is not defined, the value that we have is "cave"

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	time.sleep(3)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == (friendlyCave):
		print('Gives you his treasure!')
	else:
		print('Gobbles you down in one bite!') ### Missing parentheses, therefore could not call to print

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y': ### Syntax error (==, instead of =)
	displayIntro()
	caveNumber = chooseCave() ### "choosecave" is not defined because it should be "chooseCave()"
	checkCave(caveNumber)
    
	print('Do you want to play again? (yes or no)')
	playAgain = input()
	if playAgain == "no":
		print("Thanks for playing") ### fixed mispelled word "playing" instead of "planing"
