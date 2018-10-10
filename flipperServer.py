import soundcard as sc
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
import random

PI = np.pi  # 3.14159... (the angle of a circle)
SAMPLERATE = 44100  # A samplerate supported by nearly all devices
data = []  # Recorded data will be stored here

def getYPoints(paramY):
    """Spaces out evenly points of a Y graph from each other in order to plot them"""
    tempN = len(paramY)
    return (2.0/tempN) * np.abs(paramY[0:int(tempN/2)])


def getXPoints(paramY):
    """Gives you all the x points you need evenly spaced when given an array of Y points"""
    tempN = len(paramY)
    tempT = 1/tempN
    return np.linspace(0.0, 1.0/(2.0*tempT), int(tempN/2))


def sine_tone(frequency, default_speaker, duration=0.1, sample_rate=SAMPLERATE, channels=1):
    """
    Generate a sinewave tone, given:
    `frequency` in Hertz (Hz), a measurement of cycles/oscillations per second 
    `duration` in seconds (can be a decimal), default=0.1 seconds
    `sample_rate`, the amount of samples per, default=44100
    `channels`, the amount of audio tracks, such as a left and right channel for stereo playback, default=1 (mono sound)
    """

    sineData = []  # An empty array where we will store points on a graph

    if default_speaker != None:
        for i in np.arange(sample_rate * duration):
            sample = np.sin((2 * PI * frequency * (i / sample_rate)))
            sineData.append(sample)

        default_speaker.play(sineData/np.max(sineData),
                            samplerate=sample_rate, channels=channels)
    else:
        raise ValueError('No data found for speaker')

def recordAndPlay(default_mic=None, default_speaker=None, length=1):
    """
    Return data from microphone as an array.
    `length`: The amount of time to record, default is `1` second
    """
    print("RECORD AND PLAYBACK:")
    if default_mic == None:
        raise ValueError('No data found for microphone')
    elif default_speaker == None:
        raise ValueError('No data found for speaker')
    else:
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


def bin(flatData):
	result = random.randint(0,1)
	return result

def FFT(pData):
    """
    STORE THE MICROPHONE DATA IN A FLATTENED FORM
    """
    flatData = []
    for i in pData:
        if (i[0] != 0.0):
            flatData.append(i[0]+i[1])

    """
    RETURNS FFT
    """
    dataFFT = fft(flatData)  # Finds the FFT
    return dataFFT


