It is a sample rate convert program which converting 44100 to 32000.
From 44100 to 32000 is tricky as it is not easy to find a common ratio between these two sample rate.
This method is up-sample 8 times and down-sample 11 times.
The up-sample is via a FIR filter.
This program includes:
1) pyaudio to read write wave file
2) FIR filter
3) sample rate convert from 44100 to 32000  
4) a matlab script is also included