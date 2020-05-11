#%% IMPORTING PACKAGES
from matplotlib.pylab import *
from scipy.io import wavfile
from scipy.signal import correlate
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import xcorr
import scipy.fftpack

#import os

#os.environ["MODIN_ENGINE"] = "dask"  # Modin will use Dask - works better for windows
#import modin.pandas as pd
import pandas as pd
import matplotlib.style as style
from scipy import stats
import wavio
import seaborn as sns
import gc
import altair as alt
from altair_saver import save

import tkinter as tk
from tkinter import filedialog

# custom module below
from Fourier import Fourier
import FourierAnalysisTools as ft


#%% waveform graph with altair
def altairWaveform(w, nameOfFiles):
    root = tk.Tk()
    dirname = filedialog.askdirectory(title='Please select a directory to save your matplotlib FFT graphs')

    alt.data_transformers.disable_max_rows()
    #alt.renderers.enable('mimetype')

    for i in range(len(w)):
        timeLen = arange(0, w[i].data.shape[0], 1)
        timeLen = timeLen/w[i].rate
        y = w[i].data[:,0]

        data1 = {'Time': timeLen, 'Arbitrary intensity': y}

        source = pd.DataFrame(data=data1)

        c = alt.Chart(source).mark_line(point=False).encode(
            x = "Time", # change x-axis label
            y = "Arbitrary intensity" # change y-axis-label
        ).properties(title=nameOfFiles[i])

         # choose the directory path you want to save the files in:
        save(c, dirname+'/'+nameOfFiles[i]+'_altair_waveform'+'.png', format = 'png')


#%% FFT graph with altair
def altairFFT(w, nameOfFiles):
    root = tk.Tk()
    dirname = filedialog.askdirectory(title='Please select a directory to save your matplotlib FFT graphs')

    alt.data_transformers.disable_max_rows()
    freqArray, fftp = ft.fftMultipleFiles(w)

    for i in range(len(w)):
        intenVal = 10*log10(fftp[i])

        source = pd.DataFrame({
            'Frequency': freqArray[i],
            'Intensity': intenVal
        })

        c = alt.Chart(source).mark_line(point=False).encode(
            x = "Frequency", # change x-axis label
            y = "Intensity" # change y-axis-label
        ).properties(title=nameOfFiles[i])

        # choose the directory path you want to save the files in:
        save(c, dirname+'/'+nameOfFiles[i]+'_altair_FFT'+'.png', format = 'png')


#%% spectrogram graph with altair
def altairSpect(w, nameOfFiles):
    root = tk.Tk()
    dirname = filedialog.askdirectory(title='Please select a directory to save your matplotlib FFT graphs')

    alt.data_transformers.disable_max_rows()
    for i in range(len(w)):

        powerSpectrum, frequenciesFound, time, imageAxis = plt.specgram(w[i].data[:,0], Fs = w[i].rate)
        print(shape(time))
        print(shape(frequenciesFound))
        print(shape(powerSpectrum))
        imageAxis
        source = pd.DataFrame({
            'Time': time,
            'Frequency': frequenciesFound,
            'Power': powerSpectrum
        })
        


        c = alt.Chart(source).mark_rect().encode(
            x="Time", # change x axis label
            y="Frequency", # change y axis label
            color="Power" # change colorbar label
        ).properties(title=nameOfFiles[i])

        # choose the directory path you want to save the files in:
        save(c, dirname+'/'+nameOfFiles[i]+'_altair_spectrogram'+'.png', format = 'png')