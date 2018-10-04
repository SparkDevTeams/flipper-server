import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft


def getYPoints(paramY):
    """Spaces out evenly points of a Y graph from each other in order to plot them"""
    # Number of points in the Y array
    tempN = len(paramY)

    # A bunch of math you don't need to worry about
    return (2.0/tempN) * np.abs(paramY[0:int(tempN/2)])


def getXPoints(paramY):
    """Gives you all the x points you need evenly spaced when given an array of Y points"""
    # Number of points in the Y array
    tempN = len(paramY)

    # Horizontal spacing between points
    tempT = 1/tempN
    # Imagine showing an entire graph within the space of 1 screen
    # That's whats happening above, we're spacing out all points for them to fit in the window

    # Basically, it gives you an array of points spaced out evenly at intervals of tempN/2,
    # starting from 0 and ending at 1/twice the size of tempT in order to show you a graph
    # on a single window
    return np.linspace(0.0, 1.0/(2.0*tempT), int(tempN/2))
    # We divide tempN by 2, since FFT is symmetrically mirrored if we showed the whole graph


"""
GENERATE 3 LINES AND COMBINE THEM INTO ONE LINE
"""
N = 64  # Number of points
T = 1/N  # Spacing between points
# if T is time/distance, 1/T is frequency/wavenumber

# Just generates numbers to be used to graph a line
x = np.linspace(0, 2*np.pi*N*T, N)

# Let's take X as time, so 1/X is frequency!
y1 = np.cos(20*x)
y2 = np.sin(10*x)
y3 = np.sin(5*x)

# Produces a series of y points which are the sum of all three previous y graphs
y = y1 + y2 + y3


"""
PLOT THE GRAPH OF NORMAL Y, THE REGULAR ARRAY OF DATA
"""
# Inidcate start of first "figure", which means, first popup window
plt.figure(1)
# Everything after the previous line will only apply to
# this figure until a new figure is declared
plt.title('Regular data')
plt.plot(getXPoints(y), getYPoints(y), 'black')


"""
PLOT THE GRAPH OF THE FFT OF Y
"""
plt.figure(2)  # Create second figure/popup
# Stores the discrete Fourier transform (fft) graph of y inside of fy
ffty = fft(y)
plt.title('FFT of data')
plt.plot(getXPoints(ffty), getYPoints(ffty), 'orange')


"""
PLOT THE GRAPH OF THE IFFT OF THE FFT OF Y
"""
plt.figure(3)  # Create third figure, the Inverse FFT
plt.title('IFFT of FFT of data')

# Stores the discrete inverse Fourier transform (ifft) of the existing fft
iffty = ifft(ffty)
plt.plot(x, iffty, 'salmon')


"""
PLOT DATA AND FFT OF DATA TOGETHER ON THE SAME GRAPH
"""
plt.figure(4)
plt.plot(getXPoints(y), getYPoints(y), 'black', label="Input Data")
plt.plot(getXPoints(ffty), getYPoints(ffty), 'orange', label="FFT")
plt.legend()  # Shows a legend to use as reference


plt.show()  # Show all figures
