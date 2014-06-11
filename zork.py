loop = 3
while loop == 3:
	print("---------------------------------------------------------")
	print("Welcome to Zork - The Unofficial Python Version.")
	print("---------------------------------------------------------")
	print("You are standing in an open field west of a white house, with a boarded front door.")
	print("(A secret path leads southwest into the forest.)")
	print("There is a Small Mailbox.")

	first = input(str("What do you do? "))
	if first.lower() == ("take mailbox"):
		print("You cannot be serious.")
		loop = 4
	if first.lower() == ("open mailbox"):
		print("Opening the small mailbox reveals a leaflet.")
		loop = 4
	if first.lower() == ("go east"):
		print("The door is boarded and you cannot remove the boards.")
		loop = 4
	if first.lower() == ("open door"):
		print("The door cannot be opened.")
		loop = 4
	if first.lower() == ("take boards"):
		print("The boards are securely fastened.")
		loop = 4
	if first.lower() == ("look at house"):
		print("The house is a beautiful colonial house which is painted white. It is clear that the owners must have been extremely wealthy.")
		loop = 4
	if first.lower() == ("read leaflet"):
		print("Welcome to the Unofficial Python Version of Zork. Your mission is to find a Jade Statue.")
		loop = 4
	if first.lower() == ("go southwest"):
		loop = 8
	while loop == 4:
		if loop == 4:
			print("---------------------------------------------------------")
			print("You are standing in an open field west of a white house, with a boarded front door.")
			print("(A secret path leads southwest into the forest.)")
			print("There is a Small Mailbox.")
			second = input(str("What do you do? "))
		if second.lower() == ("take mailbox"):
			print("It is securely anchored.")
			hello = 2
		if second.lower() == ("open mailbox"):
			print("Opening the small mailbox reveals a leaflet.")
			hello = 2
		if second.lower() == ("go east"):
			print("The door is boarded and you cannot remove the boards.")
			hello = 2
		if second.lower() == ("open door"):
			print("The door cannot be opened.")
			hello = 2
		if second.lower() == ("take boards"):
			print("The boards are securely fastened.")
			hello = 2
		if second.lower() == ("look at house"):
			print("The house is a beautiful colonial house which is painted white. It is clear that the owners must have been extremely wealthy.")
			hello = 2
		if second.lower() == ("go southwest"):
			loop = 8
		if second.lower() == ("read leaflet"):
			print("Welcome to the Unofficial Python Version of Zork. Your mission is to find a Jade Statue.")
			loop = 4
		if second.lower() == ("go southwest"):
			loop = 8
	while loop == 8:
		if loop == 8:
			print("---------------------------------------------------------")
			print("This is a forest, with trees in all directions. To the east, there appears to be sunlight.")
			forest_inp = input(str("What do you do? "))
		if forest_inp.lower() == ("go west"):
			print("You would need a machete to go further west.")
			loop = 8
		if forest_inp.lower() == ("go north"):
			print("The forest becomes inpenetrable to the North.")
			loop = 8
		if forest_inp.lower() == ("go south"):
			print("Storm-tossed trees block your way.")
			loop = 8
		if forest_inp.lower() == ("go east"):
			loop = 9
	while loop == 9:
		if loop == 9:
			print("---------------------------------------------------------")
			print("You are in a clearing, with a forest surrounding you on all sides. A path leads south.")
			print("There is an open grating, descending into darkness.")
			grating_inp = input(str("What do you do? "))
		if grating_inp.lower() == ("go south"):
			print("You see a large ogre and turn around.")
			loop = 9
		if grating_inp.lower() == ("descend grating"):
			loop = 10
	while loop == 10:
		if loop == 10:
			print("---------------------------------------------------------")
			print("You are in a tiny cave with a dark, forbidding staircase leading down.")
			cave_inp = input(str("What do you do? "))
		if cave_inp.lower() == ("descend staircase"):
			loop = 11
	while loop == 11:
		if loop == 11:
			print("---------------------------------------------------------")
			print("You have entered a mud-floored room.")
			print("Lying half buried in the mud is an old trunk, bulging with jewels. There is an old trunk here, bulging with assorted jewels.")
			last_inp = input(str("What do you do? "))
		if last_inp.lower() == ("open trunk"):
			print("You have found the Jade Statue and have completed your quest!")
			exit_inp = input(str("Do you want to continue? Y/N "))
		if exit_inp.lower() == ("n"):
			import os
			quit(1)
		if exit_inp.lower() == ("y"):
			loop = 3



