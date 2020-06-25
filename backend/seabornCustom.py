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
from scipy import stats
#import wavio
import seaborn as sns; sns.set()

import tkinter as tk
from tkinter import filedialog

# custom module below
from backend.Fourier import Fourier
import backend.FourierAnalysisTools as ft

#%%
def find_nearest( array, value  ):
    array = np.asarray(array)
    idx = ( np.abs( array - value)).argmin()
    return idx

#%% FFT
def seaFFT(w, nameOfFiles):
    root = tk.Tk()
    dirname = filedialog.askdirectory(title='Please select a directory to save your seaborn FFT graphs')
    freqArray, fftp = ft.fftMultipleFiles(w)
    #arrayOfFigs = ft.arrayOfPlotly(nameOfFiles, freqArray, fftp)
    root.destroy()

    minfreq=20 # change the number to whatever minimum frequency you want to see
    maxfreq=3000 # change the number to whatever maximum frequency you want to see

    for i in range(len(fftp)):
        intenVal = 10*log10(fftp[i])
        
        #fig, axs = plt.subplots(ncols = 1)
        plt.figure(figsize=(20,10))
        #sns.lineplot(x = freqArray[i], y = intenVal, ax = axs)

        minfreqIndex = find_nearest( freqArray[i], minfreq   ) 
        maxfreqIndex = find_nearest( freqArray[i], maxfreq ) 

        freqRange = freqArray[i][minfreqIndex:maxfreqIndex+1]
        intenVal = intenVal[minfreqIndex:maxfreqIndex+1]

        sns.lineplot(x = freqRange, y = intenVal)
        
        plt.xlabel('Frequency') # change x-axis label
        plt.ylabel('Intensity') # change y-axis label
        plt.title(nameOfFiles[i])

        # choose the directory path you want to save the files in:
        plt.savefig(dirname+'/'+nameOfFiles[i]+'_seaborn_FFT'+'.png')
        plt.close(fig=None)


#%% SPECTROGRAM
'''
def seaSpect(w, nameOfFiles):
    for i in range(len(w)):
        f, t, Sxx = signal.spectrogram(w[i].data[:,0], Fs = w[i].rate)
        sns.heatmap()
'''

