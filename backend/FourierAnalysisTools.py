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
#from wavinfo import WavInfoReader
import tkinter as tk
from tkinter import filedialog
from backend.Fourier import Fourier # custom module

# new packages to add in batch file if not downloaded already
import glob
import os

#%% FUNCTION TO LOAD FILES AND THE NAMES OF FILES IN ARRAYS
def fileLoading():
    root = tk.Tk()
    dirname = filedialog.askdirectory(title='Please select a directory of WAV files you want to analyze')
    newDirName = os.path.normpath(dirname) # converts tkinter directory path to normal OS path labeling
    w = list(glob.glob(os.path.join(newDirName, '*.wav')))
    nameOfFiles = [None]*len(w)
    root.destroy()
    
    '''
    #reversing the string
    for i in w:
        for j in i[::-1]:
            print(j)

    call = int(input("Enter the number of files you want to analyze"))
    w = [None]*call
    root = tk.Tk()
    nameOfFiles = [None]*call

    for i in range(call):
        root.fileName = filedialog.askopenfilename( filetypes = (("Wave files", "*.wav"), ("All files", "*.*")) )
        nameOfFiles[i] = str(input("Enter the name of this file"))
        w[i] = root.fileName
    '''
    #renaming the files brute force
    for i in range(len(w)):
        lastChar_index = w[i].rfind("\\") # finds the index of the last occurrence of the input value - need to change per OS
        temp = w[i][lastChar_index+1:]
        secChar_index = temp.rfind(".")
        realName = temp[:secChar_index]
        nameOfFiles[i] = realName
        #res = re.findall(r'\w')
        #res = re.search('(.WAV|.wav)', fname) # looks for upper or lowercase .wav files

    for i in range(len(w)):
        w[i] = wavio.read(w[i]) # an array of wavio files
    return w, nameOfFiles

# %% FUCNTION FOR RUNNING FFTS OVER MULTIPLE FILES
def fftMultipleFiles(w):
    rates = []
    datas = []
    for i in range(len(w)):
        rates.append(w[i].rate) # an array of just the rates of each wav file
        datas.append(w[i].data) # an array of just the data of each wav file (can be 2D or not)

    fourier = [Fourier(rates[i], datas[i]) for i in range(len(w))] # makes an array of Fourier objects

    freqArray = [None]*len(w)
    fftp = [None]*len(w)
    for i in range(len(fourier)):
        freqArray[i], fftp[i] = fourier[i].fourierT() # running FFT on each Fourier object, outputs 1D freqArray and 1D intensity values
    return freqArray, fftp

#%% Creating an array of FULL FFTs of multiple files THROUGH PLOTLY
def arrayOfPlotly(nameOfFiles, freqArray, fftp):
    figArray = []
    for i in range(len(fftp)):
        fig = go.Figure()
        title = str(input("Enter the title of the graph"))
        fig.add_trace(go.Scatter(
            x = (freqArray[i]),
            y = 10*log10(fftp[i]),
            name = nameOfFiles[i]
        ))
        figArray.append(fig)

    fig.update_layout(
        title=title
    )
    
    fig.update_xaxes(title_text='Frequency (Hz)')
    fig.update_yaxes(title_text='Intensity (dB)')

    return figArray

#%% Creating an array of FULL FFTs of multiple files THROUGH MATPLOTLIB - DEBUG FUNCTION
def plotWithMatPlot(freqArray, fftp):
    figs = []
    for i in range(len(fftp)):
        intenVal = 10*log10(fftp[i])
        figs.append(plt.figure())
        ax = figs[i].add_subplot(1,i+1,1)
        ax.plot(  freqArray[i], intenVal  )
        ax.set_xlabel('Freq')
        ax.set_ylabel('Intensity')
    return plt

#%% FUNCTION TO AVERAGE FFTS
def avgFFTS(freqArray, fftp):
    lenFreqArray = []
    for i in freqArray:
        lenFreqArray.append(len(i))
    minimum = min(lenFreqArray)

    for i in range(len(fftp)):
        freqArray[i] = freqArray[i][:minimum]
        fftp[i] = fftp[i][:minimum]

    total = 0
    for i in range(len(fftp)):
        total = fftp[i] + total
        avg = total / len(fftp)
    return avg

#%% creating an array of the time of your audio file
def timeList(w):
    timeArray = arange(0, w.data.shape[0], 1)
    timeArray = timeArray / w.rate
    timeArray = timeArray*1000  #scale to milliseconds
    return timeArray

#%% SPLITTING UP ARRAY WITH GIVEN TIME MARKERS
def chunkIt(raw_wav_data, timeArray, numOfInhalations): # returning time markers for where to split up the audio files
    avg = len(timeArray)/float(numOfInhalations)
    out = []
    last = 0.0

    while last < len(timeArray):
        out.append(timeArray[int(last):int(last + avg)])
        last += avg
    
    marker = []
    num = 1
    for i in range(0,numOfInhalations):
        marker.append(num*len(out[0]))
        num +=1
    
    wavDataArray = []
    wavDataArray.append(raw_wav_data.data[0:marker[0]])
    for i in range(len(marker)-1):
        wavDataArray.append(raw_wav_data.data[marker[i]:marker[i+1]])
    
    return wavDataArray
#%%
def scanningFFTOneFile(chunksOfArray, sampFreq):

    fourier = [Fourier(sampFreq, chunksOfArray[i]) for i in range(len(chunksOfArray))]
    freqArray = [None]*len(chunksOfArray)
    fftp = [None]*len(chunksOfArray)
    for i in range(len(fourier)):
        freqArray[i], fftp[i] = fourier[i].fourierT()

    return freqArray, fftp

#%% COMPUTING AND PLOTTING POWER SPECTRAL DENSITY (PSD)
def powerSD(w):
    # https://scipy-lectures.org/intro/scipy/auto_examples/plot_spectrogram.html
    # https://scipy.github.io/devdocs/generated/scipy.signal.welch.html

    rates = []
    datas = []
    freqArray = []
    psdArray = []
    for i in range(len(w)):
        rates.append(w[i].rate)
        datas.append(w[i].data)

    for i in range(len(w)):
        freqArray.append((signal.welch(datas[i][:,0]))[0])
        psdArray.append((signal.welch(datas[i][:,0]))[1])

    '''
    plt.figure(figsize=(5, 4))
    plt.semilogx(freqArray[1], psdArray[1])
    plt.title('PSD: power spectral density')
    plt.xlabel('Frequency')
    plt.ylabel('Power')
    plt.tight_layout()
    '''
    return freqArray, psdArray

#%% READING MARKERS EMBEDDED IN WAV FILE



# %%
