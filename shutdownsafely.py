# Import the modules to send commands to the system and access GPIO pins 
from subprocess import call
import RPi.GPIO as gpio 

# Define a function to keep script running 
def loop(): 
	raw_input() 

# Define a function to run when an interrupt is called 
def shutdown(pin): 
	call('halt', shell=False) 
#	print 'pressed'

gpio.setmode(gpio.BCM) #Set pin numbering to board numbering 
gpio.setup(4, gpio.IN) # Set up pin 4 as an input 
gpio.add_event_detect(4, gpio.FALLING, callback=shutdown, bouncetime=1000) # Set up an interrupt to look for button presses 

loop() # Run the loop function to keep script running
