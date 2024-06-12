# ==========================================================================================
# Stephen Stringer 2024
# End of Code in Place Assessment Exercise
# Outline - simple pattern matching game using faces of my Code in Place team mates
# I found that in Tkinter (unlike C#) once the screen is displayed (main.Loop) code doesn't appear 
# to run unless event based.  So no main in this programme, it runs linearly until main loop
# Also it appears that the functions must appear at the top rather than the bottom, again
# it might be because of the linear flow.
# Still come improvements required on the screen refresh, which I will try to work on in the
# meantime displaying a messagebox causes the refresh after the second failed match attempt
# ==========================================================================================

# Import modules that will be required for this project
import os						# used to get the list of available graphics for the tiles
import random					# used to shuffle the cards
import time 					# used during the refresh (when implemented later)
from tkinter import *			# graphics libraries
from tkinter import messagebox	# graphics libraries
from  PIL import Image, ImageTk	# graphics libraries

# Define common variables
list_chosenEmojs = []           # create the empty ist, this will contain the randomly picked Emoj tiles
list_buttonState  = []          # This will hold the state for each button, the graphic displayed, if it's matched etc.  This is because buttons don't have tags
list_buttonimages = []			# Create a list holding the images for the tiles

list_answer = []				# Records the the two tiles selected
dict_answer = {}				# TBC
global winner 					# Global can be used in a function to define a variable as global - nasty!
winner = 0 

# Make the main screen setting the window title and size, pop on a frame that will hold the buttons
root = Tk()
root.title("Memory Tile Game by Strings")
root.geometry("500x500")
my_frame = Frame(root)			# the button (tiles) are placed in the frame with a little pladding from the edges
my_frame.pack(pady=10)


def myf_win():
	# When the user wins display a message and colour the tiles green
	my_label.config(text="Congratulations! You Win!")
	button_list = [b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11]
	for button in button_list:
		button.config(bg="green")

def button_click(b, number):
	# Define these are global, even though defined at the top of the class it doesn't work without this
	global list_answer, dict_answer, winner
	
	# If the tile is displaying the blank image and the number of tiles selected is less than two then display the actual emjoy image
	if list_buttonState[number] == "blank" and len(list_answer) < 2:
		
		b["image"] = list_buttonimages[number]

		# Update the button state trackers, add the tile to the answer list and the emjoj filename to the dict (not the file name would exist twice in the emoj list)
		list_buttonState[number] = "clicked"
		list_answer.append(number)
		dict_answer[b] = list_chosenEmojs[number]
		
	# If two answers have been selected then check for a match, if not reset the tiles to blank
	if len(list_answer) == 2:
		if list_chosenEmojs[list_answer[0]] == list_chosenEmojs[list_answer[1]]:
			# It is a match, disable the buttons and increment the match count (12 images so 6 pairs)
			my_label.config(text="It's a MATCH!")
			for key in dict_answer:
				key["state"] = "disabled"

			# Update the button status
			list_buttonState[list_answer[0]] = "matched"
			list_buttonState[list_answer[1]] = "matched"
			list_answer = []
			dict_answer = {}
			winner += 1
			# If all matched call the win function
			if winner == 6:
				myf_win()
		
		# Not a match, so reset the images
		else:
			# Update the button status
			list_buttonState[list_answer[0]] = "blank"
			list_buttonState[list_answer[1]] = "blank"

			list_answer = []
			my_label.config(text="It's not a match")

			# TODO Refresh the screen and apply a pause rather than displaying a messagebox to cause the update
			messagebox.showinfo("Nope - try again", "Sorry, you didn't find a pair.  Press ESC to try more tiles")
			
			for key in dict_answer:
				key["image"] = image_blank
			my_label.config(text=" ")
			dict_answer = {}
			
		

def myf_FormTileList():			# TESTED OKAY
	# Images must be displayed in pairs to match.  I set this project up with 22 stock images, 
	# this would # require 44 boxes on the screen as they are displayed in pairs, however this
	# would take to long to play.  So I plan to display 4 x 3 graphics, which will require 6 
	# unique images, so form a list of 6 emoj filenames at random from the 22 available
	
	list_fullListEmojs = os.listdir('images')       # get the full list of available images
	list_fullListEmojs.remove("BlankTile.gif")		# Remove the blank image from this list
	
	for iPickImages in range(0,6):
		iIndexRnd = random.randint(0,len(list_fullListEmojs)-1)   # random number based on the elements left in the list
		list_chosenEmojs.append(list_fullListEmojs[iIndexRnd])    # add this file name to our chosen list, twice
		list_chosenEmojs.append(list_fullListEmojs[iIndexRnd])

		# By default the state of each button will be blank
		list_buttonState.append("blank")
		list_buttonState.append("blank")

		list_fullListEmojs.pop(iIndexRnd)
	# Shuffle the chosen list so things are not in a easily identifiable pattern by the user
	random.shuffle(list_chosenEmojs)
	print(list_chosenEmojs)


# Now I form the tile list, this will present the image that is displayed when the tile is clicked
myf_FormTileList()

# Set up the tile graphics, image_blank is initially displayed, however when a tile is clicked or matches the underlying imageX is displayed
image_blank = PhotoImage(file = "images\BlankTile.gif")

# TODO:  Look to replace image_bX until a collection of images each holding a PhotoImage

for i in range(0,12):
	list_buttonimages.append(PhotoImage(file = "images\\" + list_chosenEmojs[i]))


# Define the twelve buttons and then position them to form a grid.  Tie these buttons to the event handlers
h_p = 100
w_p = 100

b0 = Button(my_frame, height=h_p, width=w_p, command=lambda: button_click(b0, 0), relief="groove",image = image_blank)
b1 = Button(my_frame, height=h_p, width=w_p, command=lambda: button_click(b1, 1), relief="groove",image = image_blank)
b2 = Button(my_frame, height=h_p, width=w_p, command=lambda: button_click(b2, 2), relief="groove",image = image_blank)
b3 = Button(my_frame, height=h_p, width=w_p, command=lambda: button_click(b3, 3), relief="groove",image = image_blank)
b4 = Button(my_frame, height=h_p, width=w_p, command=lambda: button_click(b4, 4), relief="groove",image = image_blank)
b5 = Button(my_frame, height=h_p, width=w_p, command=lambda: button_click(b5, 5), relief="groove",image = image_blank)
b6 = Button(my_frame, height=h_p, width=w_p, command=lambda: button_click(b6, 6), relief="groove",image = image_blank)
b7 = Button(my_frame, height=h_p, width=w_p, command=lambda: button_click(b7, 7), relief="groove",image = image_blank)
b8 = Button(my_frame, height=h_p, width=w_p, command=lambda: button_click(b8, 8), relief="groove",image = image_blank)
b9 = Button(my_frame, height=h_p, width=w_p, command=lambda: button_click(b9, 9), relief="groove",image = image_blank)
b10 = Button(my_frame, height=h_p, width=w_p, command=lambda: button_click(b10, 10), relief="groove",image = image_blank)
b11 = Button(my_frame, height=h_p, width=w_p, command=lambda: button_click(b11, 11), relief="groove",image = image_blank)


b0.grid(row=0, column=0)
b1.grid(row=0, column=1)
b2.grid(row=0, column=2)
b3.grid(row=0, column=3)
b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=1, column=3)
b8.grid(row=2, column=0)
b9.grid(row=2, column=1)
b10.grid(row=2, column=2)
b11.grid(row=2, column=3)

my_label = Label(root, text="")
my_label.pack(pady=20)

root.mainloop()