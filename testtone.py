import soundcard as sc
import numpy

PI = numpy.pi # 3.14159... (the angle of a circle)
SAMPLERATE=44100 # A samplerate supported by nearly all devices

def sine_tone(frequency, duration=0.1, sample_rate=SAMPLERATE, channels=1):
	"""
	Generate a sinewave tone, given:
	`frequency` in Hertz (Hz), a measurement of cycles/oscillations per second 
	`duration` in seconds (can be a decimal), default=0.1 seconds
	`sample_rate`, the amount of samples per, default=44100
	`channels`, the amount of audio tracks, such as a left and right channel for stereo playback, default=1 (mono sound)
	"""

	data = [] # An empty array where we will store points on a graph
	
	for i in numpy.arange(sample_rate * duration):
		sample = numpy.sin((2 * PI * frequency * (i / sample_rate)))
		data.append(sample)
	
	default_speaker.play(data/numpy.max(data), samplerate=sample_rate, channels=channels)


# print("PLAYBACK DEVICES:")
# try:
# 	speakers = sc.all_speakers()
# 	print(speakers)
# 	pass
# except Exception:
# 	print("Unable to list playback devices.")
# 	pass

print("DEFAULT PLAYBACK DEVICE:")
try:
	default_speaker = sc.default_speaker()
	print(default_speaker)
	pass
except Exception:
	print("Unable to find default playback devices.")
	pass

print() # Prints an empty line

# print("RECORDING DEVICES:")
# try:
# 	mics = sc.all_microphones()
# 	print(mics)
# 	pass
# except Exception:
# 	print("Unable to list recording devices.")
# 	pass

# print("DEFAULT RECORDING DEVICE:")
# try:
# 	default_mic = sc.default_microphone()
# 	print(default_mic)
# 	pass
# except Exception:
# 	print("Unable to find default recording device.")
# 	pass

# print()

# print("RECORD AND PLAYBACK:")
# try:
# 	print("Recording audio for 3 seconds...")
# 	data = default_mic.record(samplerate=SAMPLERATE, numframes=(SAMPLERATE*3))
# 	print("Playing back audio...")
# 	default_speaker.play(data/numpy.max(data), samplerate=SAMPLERATE)
# 	pass
# except Exception as err:
# 	print(err)
# 	if str(err).find("0x80070005") != -1:
# 		print("ERROR: Windows Permission denied when trying to access the mic.")
# 	else:
# 		print("ERROR: Unable to record and play back audio automatically.")
# 	pass

# You can explicitly set parameters to whatever you want
# However, if you enter parameters in order, you don't need to set them
# sine_tone(frequency=329.63)
# sine_tone(220.00)
# sine_tone(392.00, duration=0.4)
# sine_tone(392.00, 0.4)
# # Theres a delay here because of the time it takes to graph the sine wave for 3 seconds
# sine_tone(490, 3)
# # There is almost no delay here because the sound is so short that the graph is created quickly
# sine_tone(390, 0.1)



# sine_tone(400, 0.2)
# sine_tone(600, 0.2)
# sine_tone(800, 0.2)
# sine_tone(900, 0.2)




# # From low frequency to below human hearing
# sine_tone(50, 1)
# # Some people won't be able to hear this
# sine_tone(30, 1)
# sine_tone(20, 1)
# # Most people won't be able to hear this
# sine_tone(1, 1)
# sine_tone(0.5, 1)
# sine_tone(0.3, 1)
# sine_tone(0.01, 1)


# # From normal frequency to beyond human hearing
# sine_tone(400, 1)
# sine_tone(600, 1)
# sine_tone(1000, 1)
# # Most people won't be able to hear this
# sine_tone(18000, 1)
# sine_tone(19000, 1)
# # Pretty much nobody can hear this high, but your pets might get agitated
# sine_tone(20000, 1)
# sine_tone(20500, 1)
# sine_tone(21000, 1)






#Function to convert string to binary
def string2bits(s=''):
    return [bin(ord(x))[2:].zfill(8) for x in s]

#Function to convert binary to string
def bits2string(b=None):
    return ''.join([chr(int(x, 2)) for x in b])

#input allows us to prompt user for command input
s = input("input command \n")
#this takes the users input and translates it to binary
b = string2bits(s)

s2 = bits2string(b)
i = 0
#while i is less than the number of items in the array of bits
while i < len(b):
    #for every individual binary
    for x in b[i]:
        #emit high tone
        if x == "1":
            sine_tone(5000,0.1)
        #emit low tone
        elif x == "0":
            sine_tone(500,0.1)
        else:
            print ("error" )
    i += 1    
#print the bits for verification
print (b)
