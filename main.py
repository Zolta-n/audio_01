# This is a script to manage .wav files

from scipy.io import wavfile
import scipy.io

import sys
import matplotlib.pyplot as plt
import numpy as np
import simpleaudio as sa


sample_rate, data = wavfile.read("venv/Audio/groove-beat.wav")


print(f"The sample rate is {sample_rate} sample/sec")
length = data.shape[0] / sample_rate
# print(f"The number of channels = {data.shape[1]}")
time=np.linspace(0.,length, data.shape[0])
plt.plot(time, data)
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()

#  Play .wav file

wav_obj = sa.WaveObject.from_wave_file("venv/Audio/groove-beat.wav")
#play_obj = wav_obj.play()
play_obj = sa.play_buffer(data,1,4,44100)
print('Music is playing')
play_obj.wait_done()