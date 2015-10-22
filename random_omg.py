from sense_hat import SenseHat
import time
import random

sense = SenseHat()
r=random.randint(0,255)    #these variables could also be set once above	
r1=random.randint(0,255)   #and then just have the order changed
r2=random.randint(0,255)   #instead of being called fresh each time.
sense.show_letter("O",text_colour=[r, r1, r2])
time.sleep(1)

r=random.randint(0,255) 	
r1=random.randint(0,255)
r2=random.randint(0,255)
sense.show_letter("M",text_colour=[r2, r1, r])
time.sleep(1)

r=random.randint(0,255) 	
r1=random.randint(0,255)
r2=random.randint(0,255)
sense.show_letter("G",text_colour=[r1, r, r2])
time.sleep(1)

sense.show_letter("!", text_colour=[0, 0, 0], back_colour=[255, 255, 255])
time.sleep(1)
sense.clear()