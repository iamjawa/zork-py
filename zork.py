# Introduction narration of game


loop = 4
print("---------------------------------------------------------")
print("Welcome to Zork - The Unofficial Python Version.")

while True:
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
		elif second.lower() == ("open mailbox"):
			print("---------------------------------------------------------")
			print("Opening the small mailbox reveals a leaflet.")
		elif second.lower() == ("go east"):
			print("---------------------------------------------------------")
			print("The door is boarded and you cannot remove the boards.")
		elif second.lower() == ("open door"):
			print("---------------------------------------------------------")
			print("The door cannot be opened.")
		elif second.lower() == ("take boards"):
			print("---------------------------------------------------------")
			print("The boards are securely fastened.")
		elif second.lower() == ("look at house"):
			print("---------------------------------------------------------")
			print("The house is a beautiful colonial house which is painted white. It is clear that the owners must have been extremely wealthy.")
		elif second.lower() == ("go southwest"):
			loop = 8
		elif second.lower() == ("read leaflet"):
			print("---------------------------------------------------------")
			print("Welcome to the Unofficial Python Version of Zork. Your mission is to find a Jade Statue.")
		else:
			print("---------------------------------------------------------")
	

	# Southwest Loop
	while loop == 8:
		if loop == 8:
			print("---------------------------------------------------------")
			print("This is a forest, with trees in all directions. To the east, there appears to be sunlight.")
			forest_inp = input("What do you do? ")

		if forest_inp.lower() == ("go west"):
			print("---------------------------------------------------------")
			print("You would need a machete to go further west.")
		elif forest_inp.lower() == ("go north"):
			print("---------------------------------------------------------")
			print("The forest becomes impenetrable to the North.")
		elif forest_inp.lower() == ("go south"):
			print("---------------------------------------------------------")
			print("Storm-tossed trees block your way.")
		elif forest_inp.lower() == ("go east"):
			loop = 9
		else:
			print("---------------------------------------------------------")
	

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
		elif grating_inp.lower() == ("descend grating"):
			loop = 10
		else:
			print("---------------------------------------------------------")	


	# Grating Loop and Cave Input
	while loop == 10:
		if loop == 10:
			print("---------------------------------------------------------")
			print("You are in a tiny cave with a dark, forbidding staircase leading down.")
			print("There is a skeleton of a human male in one corner.")
			cave_inp = input("What do you do? ")

		if cave_inp.lower() == ("descend staircase"):
			loop = 11
		elif cave_inp.lower() == ("take skeleton"):
			print("---------------------------------------------------------")
			print("Why would you do that? Are you some sort of sicko?")
		elif cave_inp.lower() == ("smash skeleton"):
			print("---------------------------------------------------------")
			print("Sick person. Have some respect mate.")
		elif cave_inp.lower() == ("light up room"):
			print("---------------------------------------------------------")
			print("You would need a torch or lamp to do that.")
		elif cave_inp.lower() == ("break skeleton"):
			print("---------------------------------------------------------")
			print("I have two questions: Why and With What?")
		elif cave_inp.lower() == ("go down staircase"):
			loop = 11
		elif cave_inp.lower() == ("scale staircase"):
			loop = 11
		elif cave_inp.lower() == ("suicide"):
			print("---------------------------------------------------------")
			print("You throw yourself down the staircase as an attempt at suicide. You die.")
			print("---------------------------------------------------------")
			suicide_inp = input("Do you want to continue? Y/N ")
			if suicide_inp.lower() == ("n"):
				exit()
			if suicide_inp.lower() == ("y"):
				loop = 4
		elif cave_inp.lower() == ("scale staircase"):
			loop = 11
		else:
			print("---------------------------------------------------------")


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
		
		# Exit loop at the end of game
		exit_inp = input("Do you want to continue? Y/N ")
		if exit_inp.lower() == ("n"):
			exit()
		if exit_inp.lower() == ("y"):
			loop = 4