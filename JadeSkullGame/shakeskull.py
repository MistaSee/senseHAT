#MrC's Ninja game: Attempt to cross the classroom without setting off the Jade Skull! If he gets mad at you 3 times, you're out!
from sense_hat import SenseHat
import random
import time
import pygame

sense = SenseHat()
pygame.mixer.init()

#set up all our colours
r = [255, 0, 0]
o = [255, 127, 0]
y = [255, 255, 0]
g = [0, 255, 0]
b = [0, 0, 255] 
i = [75, 0, 130]
v = [159, 0, 255]
w = [255, 255, 255] #w is for white
n = [0, 0, 0] #n is for nothing, or black.

#set up all the images to display
image1 = [
n,n,g,g,g,g,g,n,
n,g,g,g,g,g,g,g,
g,r,n,g,r,n,g,g,
g,n,n,g,n,n,g,g,
n,g,g,n,g,g,g,n,
n,n,n,g,g,g,n,n,
n,n,n,n,n,g,n,n,
n,n,n,g,g,g,n,n
]

image2 = [
n,n,g,g,g,g,g,n,
n,g,g,g,g,g,g,g,
g,n,r,g,n,r,g,g,
g,n,n,g,n,n,g,g,
n,g,g,n,g,g,g,n,
n,n,n,g,g,g,n,n,
n,n,n,n,n,g,n,n,
n,n,n,g,g,g,n,n
]

image3 = [
n,n,g,g,g,g,g,n,
n,g,g,g,g,g,g,g,
g,n,n,g,n,n,g,g,
g,n,r,g,n,r,g,g,
n,g,g,n,g,g,g,n,
n,n,n,g,g,g,n,n,
n,n,n,n,n,g,n,n,
n,n,n,g,g,g,n,n
]

image4 = [
n,n,g,g,g,g,g,n,
n,g,g,g,g,g,g,g,
g,n,n,g,n,n,g,g,
g,r,n,g,r,n,g,g,
n,g,g,n,g,g,g,n,
n,n,n,g,g,g,n,n,
n,n,n,n,n,g,n,n,
n,n,n,g,g,g,n,n
]

cool = [
n,n,g,g,g,g,g,n,
n,g,g,g,g,g,g,g,
b,b,b,b,b,b,b,b,
g,b,b,g,b,b,g,g,
n,g,g,n,g,g,g,n,
n,n,n,g,g,g,n,n,
n,n,n,n,n,g,n,n,
n,n,n,g,g,g,n,n
]

bad = [
n,n,g,g,g,g,g,n,
n,g,g,g,g,g,g,g,
g,r,g,g,g,r,g,g,
g,r,r,g,r,r,g,g,
n,g,g,n,g,g,g,n,
n,n,n,g,g,g,n,n,
n,n,n,n,n,n,n,n,
n,n,n,g,g,g,n,n
]

#set up what happens when you trigger the accelerometer
def face():
    if i==1:
        sense.set_pixels(cool)
	pygame.mixer.music.load("/home/pi/coolsound.wav") #This relies on your having copied the sounds to your home directory
	pygame.mixer.music.play()
	time.sleep(5)
    else:
        sense.set_pixels(bad)
	pygame.mixer.music.load("/home/pi/badsound.wav")  #This relies on your having copied the sounds to your home directory
	pygame.mixer.music.play()
        time.sleep(3)

#set up animated loop of the skull looking around
def look():
    sense.set_pixels(image1)
    x, y, z = sense.get_accelerometer_raw().values()
    sense.set_pixels(image2)
    x, y, z = sense.get_accelerometer_raw().values()
    sense.set_pixels(image3)
    x, y, z = sense.get_accelerometer_raw().values()
    sense.set_pixels(image4)
    x, y, z = sense.get_accelerometer_raw().values()

while True:
    x, y, z = sense.get_accelerometer_raw().values()
    x = abs(x)
    y = abs(y)
    z = abs(z)
    i = random.randint(1,2)

    if x > 1 or y > 1 or z > 1:  #changing these 3 numbers upward will decrease the sensitivity of the game.
        face()
    else:
        look()
