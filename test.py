from random import sample
import sys
import struct
from tracemalloc import start
import numpy as np
import wave
import sounddevice as sd
import scipy.fft as sp
from zmq import device


def tuner():
  #read in wave file
  inputFile = wave.open(sys.argv[1], 'rb')
  rate = (inputFile.getframerate())/2 #samples per second
  sample = inputFile.getsampwidth() #seconds ran
  chan = inputFile.getnchannels()
  frms = inputFile.getnframes()
  #check the sample size, and only take max 2**17 and if shorter than that trim to the largest power of 2
  print("1) ", frms)
  for i in range(17, 0, -1):
    if frms<1:
      print("invalid sample")
      break
    if frms >= (2**i):
      print("found max as", 2**i)
      frms = 2**i
      break
  print("2) ", frms)
  #sample = frames/frms * sample

  #use bartlet window equation, or You can construct this window (linear increase from 0 to 1 halfway, 
  # then linear decrease to 0 at the end) manually, or get it from somewhere
  temp = inputFile.readframes(frms)
  x = np.array(struct.unpack('{n}h'.format(n=frms*inputFile.getnchannels()), temp))
  tri = np.bartlett(frms)
  filtered = sp.fft(tri*x)
  bins = np.fft.fftfreq(frms, 1/48000)
  maxbin = bins[np.argmax(np.abs(filtered))]
  cbin = maxbin * 48000/frms


  
  inputFile.close()
  #mx = abs(y)
  #Find the largest bin in the dft
  #Report the center frequency of that bin
  #maxBin = np.argmax(np.abs(y))
  
  print("Frequency: ", cbin , "hrz")

def stuner():
  frms = 8192
  istream = sd.InputStream(samplerate=48000, device=True, channels=1, dtype=np.int16)
  micfrms = []
  
  flag = False
  while not flag:
    try:
      micfrms = np.frombuffer(istream.read(frms), dtype=np.int16)
      tri = np.bartlett(frms)
      filtered = sp.fft(tri*micfrms)
      bins = np.fft.fftfreq(frms, 1/48000)
      maxbin = bins[np.argmax(np.abs(filtered))]
      cbin = maxbin * 48000/frms
      print("Frequency: ", cbin , "hrz")
    except KeyboardInterrupt:
      flag = True



def main():
  if(len(sys.argv) > 2):
    tuner()
  else:
    stuner()
#Now make a continous report

if __name__ == "__main__":
  main()
  