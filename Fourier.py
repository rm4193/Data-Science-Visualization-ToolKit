from pylab import*
from scipy.io import wavfile
from scipy.signal import correlate
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import xcorr
from scipy import fft
import scipy.fftpack
import pandas as pd
import matplotlib.style as style
import plotly.express as px
import plotly.graph_objs as go
import plotly.figure_factory as ff
import chart_studio.plotly as py
from pydub import AudioSegment # immutable objects
import mpld3
from scipy import stats
import wavio

#http://myinspirationinformation.com/uncategorized/audio-signals-in-python/

class Fourier:
    
    def __init__(self, sampFreq, sndData):
        self.sampFreq = sampFreq # frame rate
        self.sndData = sndData # signal data represented in complex sinusoids
        
    def fourierT(self):
        # https://dsp.stackexchange.com/questions/19422/why-do-we-need-to-normalize-a-wav-file-before-calculating-the-fft
        # https://stackoverflow.com/questions/32087782/how-to-normalize-wave-read-in-python
        #self.sndData = np.mean(self.sndData, axis=1) # potentially remove THIS...
        self.sndData = self.sndData/(2.**15) # change this depending on bit size (2.**[bit size-1])
        self.sndData = self.sndData[:,0] # ...FOR THIS
        ## IMPORTANT - average FFTs instead of time domain data
        n = len(self.sndData)
        #window = signal.blackmanharris(n) # SUBJECT TO CHANGE: https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.windows.blackmanharris.html#scipy.signal.windows.blackmanharris
        
        p = fft(self.sndData) # take the fourier transform, giving us the complex number representation of sine and cosine waves of FFT
        nUniquePts = int(ceil((n+1)/2.0)) # since there is a repeat in FFT, we only want unique points. Removes aliasing

        # taking the absolute value of p gives us the magnitiude of the frequency components - converts complex to real numbers
        # giving us amplitudes at each frequency points
        p = p[0:nUniquePts]
        p = abs(p)
        
        p = p / float(n) # scale by the number of points so that
                         # the magnitude does not depend on the length 
                         # of the signal or on its sampling frequency  
        p = p**2  # square it to get the power 

        # multiply by two (see technical document for details) - the reason is because when you take only half of the FFT
        # values, then the energy level is also decreased by half. Therefore, multiply odd and even FFTs by 2
        # http://samcarcagno.altervista.org/blog/basic-sound-processing-python/?doing_wp_cron=1579725639.2813010215759277343750
        # https://www.mathworks.com/matlabcentral/answers/162846-amplitude-of-signal-after-fft-operation
        # this is for FFTShifts - look into this
        # odd nfft excludes Nyquist point
        if n % 2 > 0: # we've got odd points fft
            p[1:len(p)] = p[1:len(p)] * 2
        else:
            p[1:len(p) -1] = p[1:len(p) - 1] * 2 # we've got even points fft
        
        freqArray = arange(0, nUniquePts, 1.0) * (self.sampFreq / n)
        return freqArray, p
    
    def fourierScatterSeparate(self, freqArray, p, name):
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=freqArray, 
            y=10*log10(p)[freqArray < 1000],
            name = name
        ))
        return fig
    
    def fourierScatterTogether(self, freqArray, p, name):
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=freqArray, 
            y=10*log10(p)[freqArray < 1000],
            name = name
        ))
        return fig
    
    def timeList(self):
        timeArray = arange(0, self.sndData.shape[0], 1)
        timeArray = timeArray / self.sampFreq
        timeArray = timeArray*1000  #scale to milliseconds
        return timeArray
    
    def amplitude(self):
        return self.sndData



