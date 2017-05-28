# Introduction narration of game
import string
loop = 3
while loop == 3:
	print("---------------------------------------------------------")
	print("Welcome to Zork - The Unofficial Python Version.")
	print("---------------------------------------------------------")
	print("You are standing in an open field west of a white house, with a boarded front door.")
	print("(A secret path leads southwest into the forest.)")
	print("There is a Small Mailbox.")


	# First Screen and Input
	first = input("What do you do? ")
	if first.lower() == ("take mailbox"):
		print("---------------------------------------------------------")
		print("You cannot be serious.")
		loop = 4
	if first.lower() == ("open mailbox"):
		print("---------------------------------------------------------")
		print("Opening the small mailbox reveals a leaflet.")
		loop = 4
	if first.lower() == ("go east"):
		print("---------------------------------------------------------")
		print("The door is boarded and you cannot remove the boards.")
		loop = 4
	if first.lower() == ("open door"):
		print("---------------------------------------------------------")
		print("The door cannot be opened.")
		loop = 4
	if first.lower() == ("take boards"):
		print("---------------------------------------------------------")
		print("The boards are securely fastened.")
		loop = 4
	if first.lower() == ("look at house"):
		print("---------------------------------------------------------")
		print("The house is a beautiful colonial house which is painted white. It is clear that the owners must have been extremely wealthy.")
		loop = 4
	if first.lower() == ("read leaflet"):
		print("---------------------------------------------------------")
		print("Welcome to the Unofficial Python Version of Zork. Your mission is to find a Jade Statue.")
		loop = 4
	if first.lower() == ("go southwest"):
		loop = 8
	else:
		print("---------------------------------------------------------")
		loop = 4
	

	# First Input Loop
	while loop == 4:
		if loop == 4:
			print("---------------------------------------------------------")
			print("You are standing in an open field west of a white house, with a boarded front door.")
			print("(A secret path leads southwest into the forest.)")
			print("There is a Small Mailbox.")
			second = input("What do you do? ")
		if second.lower() == ("take mailbox"):
			print("---------------------------------------------------------")
			print("It is securely anchored.")
			hello = 2
		if second.lower() == ("open mailbox"):
			print("---------------------------------------------------------")
			print("Opening the small mailbox reveals a leaflet.")
			hello = 2
		if second.lower() == ("go east"):
			print("---------------------------------------------------------")
			print("The door is boarded and you cannot remove the boards.")
			hello = 2
		if second.lower() == ("open door"):
			print("---------------------------------------------------------")
			print("The door cannot be opened.")
			hello = 2
		if second.lower() == ("take boards"):
			print("---------------------------------------------------------")
			print("The boards are securely fastened.")
			hello = 2
		if second.lower() == ("look at house"):
			print("---------------------------------------------------------")
			print("The house is a beautiful colonial house which is painted white. It is clear that the owners must have been extremely wealthy.")
			hello = 2
		if second.lower() == ("go southwest"):
			loop = 8
		if second.lower() == ("read leaflet"):
			print("---------------------------------------------------------")
			print("Welcome to the Unofficial Python Version of Zork. Your mission is to find a Jade Statue.")
			loop = 4
		if second.lower() == ("go southwest"):
			loop = 8
		else:
			print("---------------------------------------------------------")
			loop = 4
	

	# Southwest Loop
	while loop == 8:
		if loop == 8:
			print("---------------------------------------------------------")
			print("This is a forest, with trees in all directions. To the east, there appears to be sunlight.")
			forest_inp = input("What do you do? ")
		if forest_inp.lower() == ("go west"):
			print("---------------------------------------------------------")
			print("You would need a machete to go further west.")
			loop = 8
		if forest_inp.lower() == ("go north"):
			print("---------------------------------------------------------")
			print("The forest becomes impenetrable to the North.")
			loop = 8
		if forest_inp.lower() == ("go south"):
			print("---------------------------------------------------------")
			print("Storm-tossed trees block your way.")
			loop = 8
		if forest_inp.lower() == ("go east"):
			loop = 9
		else:
			print("---------------------------------------------------------")
			loop = 8
	

	# East Loop and Grating Input
	while loop == 9:
		if loop == 9:
			print("---------------------------------------------------------")
			print("You are in a clearing, with a forest surrounding you on all sides. A path leads south.")
			print("There is an open grating, descending into darkness.")
			grating_inp = input("What do you do? ")
		if grating_inp.lower() == ("go south"):
			print("---------------------------------------------------------")
			print("You see a large ogre and turn around.")
			loop = 9
		if grating_inp.lower() == ("descend grating"):
			loop = 10
		else:
			print("---------------------------------------------------------")
			loop = 9	


	# Grating Loop and Cave Input
	while loop == 10:
		if loop == 10:
			print("---------------------------------------------------------")
			print("You are in a tiny cave with a dark, forbidding staircase leading down.")
			print("There is a skeleton of a human male in one corner.")
			cave_inp = input("What do you do? ")
		if cave_inp.lower() == ("descend staircase"):
			loop = 11
		if cave_inp.lower() == ("take skeleton"):
			print("---------------------------------------------------------")
			print("Why would you do that? Are you some sort of sicko?")
			loop = 10
		if cave_inp.lower() == ("smash skeleton"):
			print("---------------------------------------------------------")
			print("Sick person. Have some respect mate.")
			loop = 10
		if cave_inp.lower() == ("light up room"):
			print("---------------------------------------------------------")
			print("You would need a torch or lamp to do that.")
			loop = 10
		if cave_inp.lower() == ("break skeleton"):
			print("---------------------------------------------------------")
			print("I have two questions: Why and With What?")
			loop = 10
		if cave_inp.lower() == ("go down staircase"):
			loop = 11
		if cave_inp.lower() == ("scale staircase"):
			loop = 11
		if cave_inp.lower() == ("suicide"):
			print("---------------------------------------------------------")
			print("You throw yourself down the staircase as an attempt at suicide. You die.")
			print("---------------------------------------------------------")
			suicide_inp = input("Do you want to continue? Y/N ")
			if suicide_inp.lower() == ("n"):
				import os
				quit(1)
			if suicide_inp.lower() == ("y"):
				loop = 3
		if cave_inp.lower() == ("scale staircase"):
			loop = 11
		else:
			print("---------------------------------------------------------")
			loop = 10


	# End of game
	while loop == 11:
		if loop == 11:
			print("---------------------------------------------------------")
			print("You have entered a mud-floored room.")
			print("Lying half buried in the mud is an old trunk, bulging with jewels.")
			last_inp = input("What do you do? ")
		if last_inp.lower() == ("open trunk"):
			print("---------------------------------------------------------")
			print("You have found the Jade Statue and have completed your quest!")
		else:
			print("---------------------------------------------------------")
			loop = 11
		
		# Exit loop at the end of game
		exit_inp = input("Do you want to continue? Y/N ")
		if exit_inp.lower() == ("n"):
			import os
			quit(1)
		if exit_inp.lower() == ("y"):
			loop = 3



