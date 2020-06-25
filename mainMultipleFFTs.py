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

import tkinter as tk
from tkinter import filedialog

# custom module below
from Fourier import Fourier
import FourierAnalysisTools as ft



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

# %%


# %%
