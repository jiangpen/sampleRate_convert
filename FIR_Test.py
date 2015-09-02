import scipy.signal as signal
import pyaudio
import wave
import sys
import numpy as np
import math
from scipy.signal import lfilter, firwin
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
sampleRate = 16000
nyq_rate = sampleRate / 2
cutoff_hz = 6000
duration=0.1
lowfreq=2000
highfreq=15000

numtaps = 29
fir_coeff = firwin(numtaps, cutoff_hz/nyq_rate)

x = np.linspace(0,duration,duration*sampleRate)


y=np.sin(lowfreq*np.pi* x) #frequent is 2K
y1=np.sin(highfreq*np.pi* x)#frequent is 15K
	
y1=y1+y
plt.figure()

filtered_y = lfilter(fir_coeff, 1.0, y1)


xx=x[:100]
yy=y1[:100]
yy1=filtered_y[:100]
yy2=y[:100]
plt.plot(xx,yy2, 'g-', label="orignal")
plt.plot(xx,yy, 'r-', label="combined")
plt.plot(xx,yy1, 'b-', label="filter Curve")

plt.legend()
plt.show()


