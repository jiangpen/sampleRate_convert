
from scipy.signal import kaiserord, lfilter, firwin, freqz

import scipy.signal as signal
import numpy as np
import pyaudio
import wave
import sys
from scipy.io import wavfile
import array
CHUNK=88
CHUNK32=64
fsin = 44100;
fsout = 32000;
N = 33;
upN = 8;
downN = 11;


taps = firwin(N, 1/upN)

#input data is 64 array of audo


if len(sys.argv) < 2:
    print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
    sys.exit(-1)
wf = wave.open(sys.argv[1], 'rb')
in_fr, in_data = wavfile.read(sys.argv[1])
in_nbits = in_data.dtype
p = pyaudio.PyAudio()

	
def sampling44100_32000( inputdata):
	xUps = np.zeros(np.ceil(CHUNK*upN))
	
	data16=np.fromstring(inputdata,dtype=np.int16)
	y =  np.zeros(CHUNK32);
	for i in range(CHUNK):
		xUps[i*upN]=data16[i]
	
	xUps = lfilter(taps, 1.0, xUps)
	for j in range(CHUNK32):
		y[j]=xUps[j*downN]
	y=y.astype(np.int16).tostring()
	return y
	
	


print(wf.getnchannels())

print(wf.getsampwidth())

outdata=[0]*CHUNK32

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=fsout,
                output=True)

data = wf.readframes(CHUNK)

while data != '':
    stream.write(data)
    data = wf.readframes(CHUNK)
    data=sampling44100_32000( data)

stream.stop_stream()
stream.close()

p.terminate()
