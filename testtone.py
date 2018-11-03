import soundcard as sc
import numpy
import os
import time
import flipper

PI = numpy.pi  # 3.14159... (the angle of a circle)
SAMPLERATE = 44100  # A samplerate supported by nearly all devices

BIT_INTERVAL_TIME = 0.15
BETWEEN_BIT_DELAY = 0.12
BETWEEN_BYTE_WAIT_TIME = 0.05

print("DEFAULT PLAYBACK DEVICE:")
try:
	default_speaker = sc.default_speaker()
	print(default_speaker)
	pass
except Exception:
	print("Unable to find default playback devices.")
	pass

print()  # Prints an empty line

print("DEFAULT RECORDING DEVICE:")
try:
	default_mic = sc.default_microphone()
	print(default_mic)
	pass
except Exception:
	print("Unable to find default recording device.")
	pass


def string2bits(s=''):
	"""Function to convert string to binary"""
	return [bin(ord(x))[2:].zfill(8) for x in s]


def string2hex(s=''):
	"""Function to convert string to binary"""
	return [hex(x)[2:].zfill(8) for x in s]


def bits2string(b=None):
	"""Function to convert binary to string"""
	return ''.join([chr(int(x, 2)) for x in b])


print("Client ready.")

default_speaker = sc.all_speakers()[1]
while True:

	# Input allows us to prompt user for command input
	s = input("Input command \n>")
	# This takes the users input and translates it to binary
	b = string2bits(s)

	s2 = bits2string(b)

	# Start timer
	t0 = time.time()
	# os.system(s2)
	i = 0
	# while i is less than the number of items in the array of bytes,
	# 	go through every byte's individual bits and play them as high and low tones
	while i < len(b):
		# for every individual binary
		for x in b[i]:
			# emit high tone
			if x == "0":
				flipper.sine_tone(19000, BIT_INTERVAL_TIME)
			# emit low tone
			elif x == "1":
				flipper.sine_tone(20050, BIT_INTERVAL_TIME)
			else:
				print("error")
			time.sleep(BETWEEN_BIT_DELAY)


		# time.sleep(BETWEEN_BYTE_WAIT_TIME)
		i += 1

	# print the bits for verification
	print(b)

	# End timer
	t1 = time.time()
	total = t1-t0
	print("(Time taken: ", total, " seconds)")
