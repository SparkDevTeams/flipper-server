import soundcard as sc
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
import os
import random
import flipperServer as flpr
import sys


PI = np.pi  # 3.14159... (the angle of a circle)
SAMPLERATE = 44100  # A samplerate supported by nearly all devices
data = []  # Recorded data will be stored here

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


# print("RECORDING DEVICES:")
# try:
# 	mics = sc.all_microphones()
# 	print(mics)
# 	pass
# except Exception:
# 	print("Unable to list recording devices.")
# 	pass

print("DEFAULT RECORDING DEVICE:")
try:
    default_mic = sc.default_microphone()
    print(default_mic)
    pass
except Exception:
    print("Unable to find default recording device.")
    pass

# Store microphone data for 2 seconds into data array
try:
    data = flpr.recordAndPlay(default_mic, default_speaker, 2)
except ValueError as err:
    sys.exit(err)

# Plot data BEFORE loading file containing ambient sounds
flpr.plotDataAndFFT(data)

# load from file
data = np.load(os.path.join("data", 'ambient18000.npy'))

#Store in file
#np.save(os.path.join("data", 'test1.npy'), data)



# TODO: Create a function that will play the data, when it is given as a parameter


# Plot data AFTER loading file containing ambient sounds
flpr.plotDataAndFFT(data)


dataFFT = flpr.FFT(data)

#checks if frequency is between 9900 and 10000
index = 9900
while index < 10000:
    index = index + 1
    if dataFFT[index] >= 10:
        print ("0")
        break

#checks if frequency is between 17900 and 18000
index = 17900
while index < 18000:
    index = index + 1
    if dataFFT[index] >= 10:
        print(dataFFT[index])
        print ("1")
        break


"""
SINE TONE GENERATION EXAMPLES
"""
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