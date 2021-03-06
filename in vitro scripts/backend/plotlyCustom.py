#%% IMPORTING PACKAGES
#from pylab import*
from matplotlib.pylab import *
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
from backend.Fourier import Fourier
import backend.FourierAnalysisTools as ft


def plotlyFFT(w, nameOfFiles):
    freqArray, fftp = ft.fftMultipleFiles(w)
    #arrayOfFigs = ft.arrayOfPlotly(nameOfFiles, freqArray, fftp)

    for i in range(len(w)):
        fig = go.Figure()
        title = nameOfFiles[i]
        fig.add_trace(go.Scatter(
            x = (freqArray[i]),
            y = 10*log10(fftp[i]),
            name = nameOfFiles[i]
        ))
        fig.update_layout(
            title=title
        )

        fig.update_xaxes(title_text= 'Frequency' ) # change x-axis label
        fig.update_yaxes(title_text= 'Intensity' ) # change y-axis label

        fig.show()

def plotlyWaveform(w, nameOfFiles):
    for i in range(len(w)):
        timeLen = arange(0, w[i].data.shape[0], 1)
        timeLen = timeLen/w[i].rate
        y = w[i].data[:,0]
        fig = go.Figure()
        title = nameOfFiles[i]
        fig.add_trace(go.Scatter(
            x = timeLen,
            y = y,
            name = nameOfFiles[i]
        ))

        fig.update_layout(
            title=title
        )
        
        fig.update_xaxes(title_text= 'Time' ) # change x-axis label
        fig.update_yaxes(title_text='Arbitrary intensity' ) # change y-axis label

        fig.show()

def stftCustom(w1, nameOfFiles):

    numOfChunks = 8 # how many chunks do you want to split STFT into

    for i in range(len(w1)):
        title = nameOfFiles[i]
        timeArray1 = ft.timeList(w1[i])
        #%% Short time Fourier Transform (STFT) over the file
        w1_chunks1 = ft.chunkIt(w1[i], timeArray1, numOfChunks)
        freqArray1, fftp1 = ft.scanningFFTOneFile(w1_chunks1, w1[i].rate)

        #%% Plotting STFT over ONE file
        fig1 = go.Figure()

        for i in range(len(fftp1)):
            fig1.add_trace(go.Scatter(
                x = freqArray1[i],
                y = 10*np.log10(fftp1[i])
            ))

        fig1.update_layout(
            title=title,
        )

        fig1.update_xaxes(title_text='Frequency (Hz)') # change x-axis title
        fig1.update_yaxes(title_text='Intensity (dB)') # change y-axis title
        fig1.show()

'''
#%% MAIN FFT
w, nameOfFiles = ft.fileLoading() # creates an array of files and array of names for each file
freqArray, fftp = ft.fftMultipleFiles(w)
#arrayOfFigs = ft.arrayOfPlotly(nameOfFiles, freqArray, fftp)

#%%
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