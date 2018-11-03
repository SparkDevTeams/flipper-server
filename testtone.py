import soundcard as sc
import numpy
import os
import time
import flipper

PI = numpy.pi  # 3.14159... (the angle of a circle)
SAMPLERATE = 44100  # A samplerate supported by nearly all devices


STABILITY = 1

if STABILITY == 0:
	BIT_INTERVAL_TIME = 0.145
	BETWEEN_BIT_DELAY = 0.16
elif STABILITY == 1:
	BIT_INTERVAL_TIME = 0.3
	BETWEEN_BIT_DELAY = 0.2
elif STABILITY == 2:
	BIT_INTERVAL_TIME = 0.46
	BETWEEN_BIT_DELAY = 0.32
elif STABILITY == 3:
	BIT_INTERVAL_TIME = 0.5
	BETWEEN_BIT_DELAY = 0.4
elif STABILITY == 4:
	BIT_INTERVAL_TIME = 0.9
	BETWEEN_BIT_DELAY = 0.6


BETWEEN_BYTE_WAIT_TIME = 0.0

FQ_0 = 17800
FQ_1 = 17950
FQ_2 = 18100
FQ_3 = 18250
FQ_4 = 18400
FQ_5 = 18550
FQ_6 = 18700
FQ_7 = 18850
FQ_8 = 19000
FQ_9 = 19150
FQ_A = 19300
FQ_B = 19450
FQ_C = 19600
FQ_D = 19750
FQ_E = 19900
FQ_F = 20050

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
    result = [hex(ord(x))[2:] for x in s]
    return result
    # return [hex(x)[2:].zfill(8) for x in s]


def bits2string(b=None):
    """Function to convert binary to string"""
    return ''.join([chr(int(x, 2)) for x in b])


print("Client ready.")

default_speaker = sc.all_speakers()[1]
while True:

    # Input allows us to prompt user for command input
    s = input("Input command \n>")
    # This takes the users input and translates it to binary
    b = string2hex(s)

    # s2 = bits2string(b)

    # Start timer
    t0 = time.time()
    # os.system(s2)
    i = 0
    # while i is less than the number of items in the array of bytes,
    # go through every byte's individual bits and play them as high and low tones
    for i in b:
        for x in i:
            if x == "0":
                flipper.sine_tone(FQ_0, BIT_INTERVAL_TIME)
            elif x == "1":
                flipper.sine_tone(FQ_1, BIT_INTERVAL_TIME)
            elif x == "2":
                flipper.sine_tone(FQ_2, BIT_INTERVAL_TIME)
            elif x == "3":
                flipper.sine_tone(FQ_3, BIT_INTERVAL_TIME)
            elif x == "4":
                flipper.sine_tone(FQ_4, BIT_INTERVAL_TIME)
            elif x == "5":
                flipper.sine_tone(FQ_5, BIT_INTERVAL_TIME)
            elif x == "6":
                flipper.sine_tone(FQ_6, BIT_INTERVAL_TIME)
            elif x == "7":
                flipper.sine_tone(FQ_7, BIT_INTERVAL_TIME)
            elif x == "8":
                flipper.sine_tone(FQ_8, BIT_INTERVAL_TIME)
            elif x == "9":
                flipper.sine_tone(FQ_9, BIT_INTERVAL_TIME)
            elif x == "a":
                flipper.sine_tone(FQ_A, BIT_INTERVAL_TIME)
            elif x == "b":
                flipper.sine_tone(FQ_B, BIT_INTERVAL_TIME)
            elif x == "c":
                flipper.sine_tone(FQ_C, BIT_INTERVAL_TIME)
            elif x == "d":
                flipper.sine_tone(FQ_D, BIT_INTERVAL_TIME)
            elif x == "e":
                flipper.sine_tone(FQ_E, BIT_INTERVAL_TIME)
            elif x == "f":
                flipper.sine_tone(FQ_F, BIT_INTERVAL_TIME)
            else:
                print("error")
            time.sleep(BETWEEN_BIT_DELAY)

        # time.sleep(BETWEEN_BYTE_WAIT_TIME)
    print(b)

    # End timer
    t1 = time.time()
    total = t1-t0
    print("(Time taken: ", total, " seconds)")
