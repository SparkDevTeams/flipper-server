import soundcard as sc
import numpy

SAMPLERATE=44100

print("PLAYBACK DEVICES:")
try:
	speakers = sc.all_speakers()
	print(speakers)
	pass
except Exception:
	print("Unable to list playback devices.")
	pass

print("DEFAULT PLAYBACK DEVICE:")
try:
	default_speaker = sc.default_speaker()
	print(default_speaker)
	pass
except Exception:
	print("Unable to find default playback devices.")
	pass

print()

print("RECORDING DEVICES:")
try:
	mics = sc.all_microphones()
	print(mics)
	pass
except Exception:
	print("Unable to list recording devices.")
	pass

print("DEFAULT RECORDING DEVICE:")
try:
	default_mic = sc.default_microphone()
	print(default_mic)
	pass
except Exception:
	print("Unable to find default recording device.")
	pass

print()

print("RECORD AND PLAYBACK:")
try:
	print("Recording audio for 3 seconds...")
	data = default_mic.record(samplerate=SAMPLERATE, numframes=(SAMPLERATE*3))
	print("Playing back audio...")
	default_speaker.play(data/numpy.max(data), samplerate=SAMPLERATE)
	pass
except Exception as err:
	print(err)
	if str(err).find("0x80070005") != -1:
		print("ERROR: Windows Permission denied when trying to access the mic.")
	else:
		print("ERROR: Unable to record and play back audio automatically.")
	pass