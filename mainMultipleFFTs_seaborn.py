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
import seaborn as sns; sns.set()

import tkinter as tk
from tkinter import filedialog

# custom module below
from Fourier import Fourier
import FourierAnalysisToolsForPackage as ft

'''
#%% MAIN FFT
w, nameOfFiles = ft.fileLoading() # creates an array of files and array of names for each file
freqArray, fftp = ft.fftMultipleFiles(w)
#arrayOfFigs = ft.arrayOfPlotly(nameOfFiles, freqArray, fftp)

#%% LINE PLOT
for i in range(len(fftp)):
    fig, axs = plt.subplots(ncols = 1)
    intenVal = 10*log10(fftp[i])
    sns.lineplot(x = freqArray[i], y = intenVal, ax = axs)

#plt.show()
'''

#%%
def seaFFT():
    #%% MAIN FFT
    w, nameOfFiles = ft.fileLoading() # creates an array of files and array of names for each file
    freqArray, fftp = ft.fftMultipleFiles(w)
    #arrayOfFigs = ft.arrayOfPlotly(nameOfFiles, freqArray, fftp)

    for i in range(len(fftp)):
        fig, axs = plt.subplots(ncols = 1)
        intenVal = 10*log10(fftp[i])
        sns.lineplot(x = freqArray[i], y = intenVal, ax = axs)
        plt.xlabel("Frequency (Hertz)")
        plt.ylabel("Intensity (Decibels)")


#%% SPECTROGRAM






