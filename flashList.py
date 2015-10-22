#Multi-coloured flash message - MrC's version
from sense_hat import SenseHat
import random
import time

sense=SenseHat()
message = [“H”,”a”,”c”,”k”,”l”,”a”,”b”,” “,”I”,”s”,” “,”A”,”w”,”e”,”s”,”o”,”m”,”e”,”!”]

while True:
	for i in message:
		r=random.randint(0,255)      			#Defining these variables inside the while loop but
		r1=random.randint(0,255)     			#above the for statement will result in the whole message
		r2=random.randint(0,255)     			#being one colour, but changing colour between messages.
		sense.show_letter( i, text_colour = [r,r1,r2])	#Putting them here gives each letter a new colour.
		time.sleep(0.5)
