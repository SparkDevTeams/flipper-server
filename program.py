import soundcard as sc
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
import os


PI = np.pi  # 3.14159... (the angle of a circle)
SAMPLERATE = 44100  # A samplerate supported by nearly all devices
data = []  # Recorded data will be stored here


# Refer to GraphExplanation.py for help with these two functions
def getYPoints(paramY):
    """Spaces out evenly points of a Y graph from each other in order to plot them"""
    tempN = len(paramY)
    return (2.0/tempN) * np.abs(paramY[0:int(tempN/2)])


def getXPoints(paramY):
    """Gives you all the x points you need evenly spaced when given an array of Y points"""
    tempN = len(paramY)
    tempT = 1/tempN
    return np.linspace(0.0, 1.0/(2.0*tempT), int(tempN/2))


def sine_tone(frequency, duration=0.1, sample_rate=SAMPLERATE, channels=1):
    """
    Generate a sinewave tone, given:
    `frequency` in Hertz (Hz), a measurement of cycles/oscillations per second 
    `duration` in seconds (can be a decimal), default=0.1 seconds
    `sample_rate`, the amount of samples per, default=44100
    `channels`, the amount of audio tracks, such as a left and right channel for stereo playback, default=1 (mono sound)
    """

    sineData = []  # An empty array where we will store points on a graph

    for i in np.arange(sample_rate * duration):
        sample = np.sin((2 * PI * frequency * (i / sample_rate)))
        sineData.append(sample)

    default_speaker.play(sineData/np.max(sineData),
                         samplerate=sample_rate, channels=channels)


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


def recordAndPlay(length=1):
    """
    Return data from microphone as an array.
    `length`: The amount of time to record, default is `1` second
    """
    print("RECORD AND PLAYBACK:")
    try:
        print("Recording audio for " + str(length) + " second(s)...")
        tempData = default_mic.record(
            samplerate=SAMPLERATE, numframes=(SAMPLERATE * length))
        print("Playing back audio...")
        default_speaker.play(tempData/np.max(tempData), samplerate=SAMPLERATE)
        return tempData
    except Exception as err:
        print(err)
        if str(err).find("0x80070005") != -1:
            print("ERROR: Windows Permission denied when trying to access the mic.")
        else:
            print("ERROR: Unable to record and play back audio automatically.")
        pass


def plotDataAndFFT(pData):
    """Plots given data array along with it's FFT"""

    """
    STORE THE MICROPHONE DATA IN A FLATTENED FORM
    """
    print('Processing data from microphone...')
    flatData = []
    for i in pData:
        if (i[0] != 0.0):
            flatData.append(i[0]+i[1])

    """
    GENERATE THE DISCRETE FOURIER TRANSFORM OF THE FLATTENED DATA
    """
    print('Generating FFT of data...')
    dataFFT = fft(flatData)  # Finds the FFT

    """
    PLOT DATA AND FFT
    """
    print('Plotting...')
    plt.figure(1)
    plt.plot(getXPoints(flatData), getYPoints(flatData), 'black')
    plt.title('Data - Audio Recording')
    plt.xlabel('Time')
    plt.ylabel('Volume')

    plt.figure(2)
    plt.plot(getXPoints(dataFFT), getYPoints(dataFFT), 'orange')
    plt.title('FFT of data')
    plt.xlabel('Actual Frequency')
    plt.ylabel('Prevalence of Frequency')

    print('Figures have been plotted.')
    plt.show()  # Show all figures


# Store microphone data for 2 seconds into data array
data = recordAndPlay(2)


# Plot data BEFORE loading file containing ambient sounds
plotDataAndFFT(data)

# load from file
data = np.load(os.path.join("data", 'ambientScreams.npy'))

#Store in file
#np.save(os.path.join("data", 'test1.npy'), data)



# TODO: Create a function that will play the data, when it is given as a parameter


# Plot data AFTER loading file containing ambient sounds
plotDataAndFFT(data)

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
