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
from Fourier import Fourier
import FourierAnalysisTools as ft


#%% FFT
def seaFFT(w, nameOfFiles):
    root = tk.Tk()
    dirname = filedialog.askdirectory(title='Please select a directory to save your matplotlib spectrograms')
    freqArray, fftp = ft.fftMultipleFiles(w)
    #arrayOfFigs = ft.arrayOfPlotly(nameOfFiles, freqArray, fftp)

    for i in range(len(fftp)):
        intenVal = 10*log10(fftp[i])
        
        #fig, axs = plt.subplots(ncols = 1)
        plt.figure(figsize=(20,10))
        #sns.lineplot(x = freqArray[i], y = intenVal, ax = axs)
        sns.lineplot(x = freqArray[i], y = intenVal)
        
        plt.xlabel('Frequency') # change x-axis label
        plt.ylabel('Intensity') # change y-axis label
        plt.title(nameOfFiles[i])
        plt.savefig(dirname+'/'+nameOfFiles[i]+'_seaborn_fft'+'.png')
        plt.close()


#%% SPECTROGRAM


