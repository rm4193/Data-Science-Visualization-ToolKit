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
#import chart_studio.plotly as py
#from pydub import AudioSegment # immutable objects
#import mpld3
from scipy import stats
import wavio
import seaborn as sns

import tkinter as tk
from tkinter import filedialog

# custom module below
from Fourier import Fourier
import FourierAnalysisTools as ft


#%% 
def matplotFFT(w, nameOfFiles):
    freqArray, fftp = ft.fftMultipleFiles(w)
    #arrayOfFigs = ft.arrayOfPlotly(nameOfFiles, freqArray, fftp)

    for i in range(len(fftp)):
        intenVal = 10*log10(fftp[i])
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        ax.plot(  freqArray[i], intenVal  )
        ax.set_xlabel('Frequency') # change x-axis label
        ax.set_ylabel('Intensity') # change y-axis label
        plt.title(nameOfFiles[i])
    
    plt.show()

#%%
def matplotSpectrogram(w, nameOfFiles):
    freqArray, fftp = ft.fftMultipleFiles(w)

    for i in range(len(fftp)):
        fig, ax = plt.subplots(nrows = 1)
        powerSpectrum, frequenciesFound, time, imageAxis = ax.specgram(w[i].data[:,0], Fs = w[i].rate)
        ax.set_xlabel('Time') # change x-axis label
        ax.set_ylabel('Frequency') # change y-axis label
        plt.title(nameOfFiles[i])




#%%
'''
figs = []
for i in range(len(fftp)):
    fig = go.Figure()
    figs.append(fig)

for i in range(len(figs)):
    figs[i]
    title = str(input("Enter the title of the graph"))
    figs[i].add_trace(go.Scatter(
        x = (freqArray[i]),
        y = 10*log10(fftp[i])
        #name = nameOfFiles[i]
    ))
    figs[i].update_layout(
        title=title
    )
    figs[i].update_xaxes(title_text='Frequency (Hz)')
    figs[i].update_yaxes(title_text='Intensity (dB)')
    
for i in range(len(figs)):
    figs[i]
'''




'''
#%% MAIN FFT
w, nameOfFiles = ft.fileLoading() # creates an array of files and array of names for each file
freqArray, fftp = ft.fftMultipleFiles(w)
#arrayOfFigs = ft.arrayOfPlotly(nameOfFiles, freqArray, fftp)

#%% LINE GRAPH
for i in range(len(fftp)):
    intenVal = 10*log10(fftp[i])
    fig = plt.figure()
    ax = fig.add_subplot(1,2,1)
    ax.plot(  freqArray[i], intenVal  )
    ax.set_xlabel('Freq')
    ax.set_ylabel('Intensity')

plt.show()


#Based on this, it is easier to output multiple graphs at the same time, using matplotlib.
#Notes:
#1) 


#%% SPECTROGRAM
for i in range(len(fftp)):
    fig, ax1 = plt.subplots(nrows = 1)
    powerSpectrum, frequenciesFound, time, imageAxis = ax1.specgram(w[i].data[:,0], Fs = w[i].rate)
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Frequency')
'''

