#%% IMPORTING PACKAGES
from pylab import*
from scipy.io import wavfile
from scipy.signal import correlate
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import xcorr
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
import seaborn as sns
import pywt
import scaleogram as scale

import tkinter as tk
from tkinter import filedialog

# custom module below
from Fourier import Fourier
import FourierAnalysisTools as ft
import waveletFunction as waveletF

#%%
w, nameOfFiles = ft.fileLoading()
#%%
coeffs, freqs, sig, rate, sampPeriod, timeArray = waveletF.wavelets(w, nameOfFiles)
#%%
waveletF.contourWavelet(coeffs, timeArray, freqs, nameOfFiles)
#%%
waveletF.heatMapWavelet(coeffs, nameOfFiles)




#%% Main
#ZOOM31 - AS 1
#ZOOM33 - HOCM OBS 1
#ZOOM42 - AS 2
#ZOOM47 - HOCM OBS 3




#%% Short time Fourier Transform (STFT) over the file
#ZOOM31 - AS 1
#ZOOM33 - HOCM OBS 1
#ZOOM42 - AS 2
#ZOOM47 - HOCM OBS 3

w1_chunks1 = ft.chunkIt(w[0], timeArray, 4)
freqArray1, fftp1 = ft.scanningFFTOneFile(w1_chunks1, rate)

fig1 = go.Figure()

for i in range(len(fftp1)):
    fig1.add_trace(go.Scatter(
        x = freqArray1[i],
        y = 10*log10(fftp1[i])
    ))

fig1.update_layout(
    title="HOCM-01 Rolling FFT",
)

fig1.update_xaxes(title_text='Frequency (Hz)')
fig1.update_yaxes(title_text='Intensity (dB)')


#%% Spectrogram
freqArray, fftp = ft.fftMultipleFiles(w)
fig, ax1 = plt.subplots(nrows = 1)
powerSpectrum, frequenciesFound, time, imageAxis = ax1.specgram(w[0].data[:,0], Fs = w[0].rate)
ax1.set_xlabel('Time')
ax1.set_ylabel('Frequency')


# %% normal plot of frequency vs. intensity of wavelet
fig = go.Figure()
title = 'test'

fig.add_trace(go.Scatter(
    x = freqs,
    y = abs(coeffs)
))

fig.update_layout(
    title=title,
)

fig.update_xaxes(title_text='Frequency (Hz)')
fig.update_yaxes(title_text='Intensity (dB)')


# %%




#%%

#%% IMPORTING PACKAGES
from pylab import*
from scipy.io import wavfile
from scipy.signal import correlate
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import xcorr
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
import seaborn as sns
import pywt
import scaleogram as scale

import tkinter as tk
from tkinter import filedialog

# custom module below
from Fourier import Fourier
import FourierAnalysisTools as ft

#%%
sig = []
rate = []
sampPeriod = []
timeArray = []
coeffs = []
freqs = []
w, nameOfFiles = ft.fileLoading()

#%%
for i in range(len(w)):
    sig.append(w[i].data[:,0])
    rate.append(w[i].rate)
    sampPeriod.append(1/rate[i])
    timeArray.append(ft.timeList(w[i]))

# Wavelet calculation
minScaleLimit = 80
maxScaleLimit = 2000
widths = np.arange(minScaleLimit, maxScaleLimit)
# widths = np.arange(10, 1000)
for i in range(len(w)):
    tempCoeffs, tempFreqs = scale.fastcwt(sig[i], widths, 'morl', sampling_period=sampPeriod[i])
    coeffs.append(tempCoeffs)
    freqs.append(tempFreqs)
    # converting scale coefficents to frequency: 
    #pywt.scale2frequency('morl', widths) / (sampPeriod)
    #normalCoeffs = coeffs
    #coeffs[:,0] = freqs

#%%
power = []
normalizedCoeffs = []
normalizedPower = []
perc = []
sumT = 0
for i in range(len(coeffs)):
    power.append((abs(coeffs[i])) ** 2) # arbitrary units for energy
    normalizedCoeffs.append(coeffs[i]/np.abs(coeffs[i]).max()) # normalization factor of the coefficients
    normalizedPower.append(power[i]/np.abs(power[i]).max())

# the below for loop needs to be fixed to accomodate for percentage of energy of each coefficient
newT = 0
for i in range(len(power)):
    100*power[i]
    for j in range(len(power[i])):
        sumT = sumT + power[i]
        newT = newT + ((100*power[i])/sumT)
    perc.append(newT)

for i in range(len(coeffs)):
    #plt.contourf(timeArray[i], freqs[i], normalizedPower[i], cmap='hot')
    plt.contourf(timeArray[i], freqs[i], normalizedCoeffs[i], cmap='hot')
    #plt.contourf(timeArray[i], freqs[i], coeffs[i], cmap='hot')
    #plt.contourf(timeArray[i], freqs[i], power[i], cmap='hot')
    
    plt.colorbar()
    plt.title(nameOfFiles[i])
    #plt.xlabel(str(input("Enter x axis name for contour plot: ")))
    plt.xlabel("Time (ms)")
    #plt.ylabel(str(input("Enter y axis name for contour plot: ")))
    plt.ylabel("Frequency (Hz)")
    plt.show()
    #plt.yscale('log')

# %%
