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
import gc

import tkinter as tk
from tkinter import filedialog

# custom module below
from backend import Fourier as Fourier
import backend.FourierAnalysisTools as ft
import backend.matplotlibCustom as matCustom
import backend.plotlyCustom as plotCustom
import backend.seabornCustom as seaCustom
import backend.waveletFunction as waveletF
import backend.bokeh_tools as bokeh
import backend.altairCustom as altairM
import backend.override_matplotlib_spect as over

import librosa
#%%
def matplotFFT(w, nameOfFiles):
    root = tk.Tk()
    dirname = filedialog.askdirectory(title='Please select a directory to save your matplotlib FFT graphs')
    freqArray, fftp = ft.fftMultipleFiles(w)
    #arrayOfFigs = ft.arrayOfPlotly(nameOfFiles, freqArray, fftp)

    minFreq = 5 # change minimum frequency you want to see in FFT graph
    maxFreq = 500 # change maximum frequency you want to see in FFT graph

    for i in range(len(fftp)):

        cols = ['Freq', 'Intensity']
        df = pd.DataFrame(columns=cols)

        intenVal = librosa.power_to_db(  np.abs(fftp[i]), ref=np.max   )
        #intenVal = librosa.power_to_db(  np.abs(fftp[i])  )
        # intenVal = 10*log10(fftp[i])

        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)

        df['Freq'] = freqArray[i]
        df['Intensity'] = intenVal
        freqData = df['Freq'].values.tolist()
        intensities = df['Intensity'].values.tolist()

        freqs = freqArray[i][ freqArray[i] > minFreq ]
        freqs = freqs[ freqs < maxFreq  ]

        startIndex = freqData.index(freqs[0])
        endIndex = freqData.index(freqs[len(freqs)-1])

        intensities = intensities[startIndex:endIndex+1]
       # newInten = newInten[ freqArray[i] < 2000  ]

        ax.plot(  freqs, intensities  )
        #ax.plot(  freqArray[i], intenVal  )
        ax.set_xlabel('Frequency') # change x-axis label
        ax.set_ylabel('Intensity') # change y-axis label
        plt.title(nameOfFiles[i])
        

        # choose the directory path you want to save the files in:
        plt.savefig(dirname+'/'+nameOfFiles[i]+'_matplot_FFT_2'+'.png')

        # outputting the graph in VS code cells
        plt.close()

#%% Choose files and name the files (click shift+enter to run cell)
w, nameOfFiles = ft.fileLoading() # creates an array of files and array of names for each file
print("All WAV files have been imported successfully!")
matplotFFT(w, nameOfFiles)


# %%
