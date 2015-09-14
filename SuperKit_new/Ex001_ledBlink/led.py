#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

LedPin = 11

GPIO.setmode(GPIO.BOARD)	# Numbers GPIOs by physical location
GPIO.setup(LedPin, GPIO.OUT)	# Set LedPin's MODE as OUT
GPIO.output(LedPin, GPIO.HIGH)	# Set LedPin as HIGH +3.3v to turn LED off

try:
	while True:
		print 'led ON'
		GPIO.output(LedPin, GPIO.LOW)	# turn LED on
		time.sleep(0.1)
		print 'led OFF'
		GPIO.output(LedPin, GPIO.HIGH)	# turn LED off
		time.sleep(0.5)
except KeyboardInterrupt:	# When CTRL-C is detected, the following
				# code will be executed.
	print 'CTRL-C detected. Cleaning up and exiting.'
	GPIO.output(LedPin, GPIO.HIGH)	# turn LED off
	GPIO.cleanup()			# Release resources

