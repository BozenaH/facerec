"""Raspberry Pi Face Recognition Treasure Box
Treasure Box Class
Copyright 2013 Tony DiCola 
"""
import time

import cv2
import RPi.GPIO as GPIO

import picam
import config
import face


class Box(object):
	"""Class to represent the state and encapsulate access to the hardware of 
	the treasure box."""
	def __init__(self):
		# Initialize lock servo and button.
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(config.BUTTON_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
		# Set initial box state.
		self.button_state = GPIO.input(config.BUTTON_PIN)
		

	def is_button_up(self):
		"""Return True when the box button has transitioned from down to up (i.e.
		the button was pressed)."""
		old_state = self.button_state
		self.button_state = GPIO.input(config.BUTTON_PIN)
		# Check if transition from down to up
		if ((not old_state) and self.button_state):
			# Wait 20 milliseconds and measure again to debounce switch.
			time.sleep(20.0/1000.0)
			self.button_state = GPIO.input(config.BUTTON_PIN)
			if self.button_state == True: 
				return True
		return False
