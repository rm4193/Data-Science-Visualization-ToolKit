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
w, nameOfFiles = ft.fileLoading() # creates an array of files and array of names for each file

#%%
freqArray, fftp = ft.fftMultipleFiles(w)
#arrayOfFigs = ft.arrayOfPlotly(nameOfFiles, freqArray, fftp)

for i in range(len(fftp)):
    intenVal = 10*log10(fftp[i])
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot(  freqArray[i], intenVal  )
    ax.set_xlabel('freq') # change x-axis label
    ax.set_ylabel('Frequency') # change y-axis label
    plt.title(nameOfFiles[i])

plt.show()

# %%
