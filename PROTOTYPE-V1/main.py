#%% IMPORTING PACKAGES (click shift+enter to run cell)
from pylab import*
from scipy.io import wavfile
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
import pandas as pd
import matplotlib.style as style
import plotly.graph_objs as go
import plotly.figure_factory as ff
import chart_studio.plotly as py
from pydub import AudioSegment # immutable objects
from scipy import stats
import wavio
import seaborn as sns

import tkinter as tk
from tkinter import filedialog

# custom module below
from Fourier import Fourier
import FourierAnalysisTools as ft
import matplotlibCustom as matCustom
import plotlyCustom as plotCustom
import seabornCustom as seaCustom
import waveletFunction as waveletF
import bokeh_tools as bokeh



#%% Choose files and name the files (click shift+enter to run cell)
w, nameOfFiles = ft.fileLoading() # creates an array of files and array of names for each file

#%% Visualization tool choice section (click shift+enter to run cell)
options = ['Plotly FFT', 'Matplot FFT', 'Matplot Spectrogram', 'Seaborn FFT', 'Matplotlib contour plot of wavelet', 'Plotly Waveform', 'Bokeh FFT']
print("The list of the different types of graphs:")
print("\n")
for j in range(len(options)):
    print(options[j])

num = int(input("How many DIFFERENT TYPES of graphs do you want? The types of graphs are shown below."))

for j in range(num):
    print("\nSelect a number for the corresponding graph you want")
    for i in range(len(options)):
        print(str(i+1) + ":", options[i]) 

    inp = int(input("Enter a number: "))

    if inp == 1:
        print("\nUsing Plotly, here is the FFT: ")
        plotCustom.plotlyFFT(w, nameOfFiles)
    elif inp == 2:
        print("\nUsing Matplotlib, here is the FFT: ")
        matCustom.matplotFFT(w, nameOfFiles)
    elif inp == 3:
        print("\nUsing Matplotlib, here is the spectrogram: ")
        matCustom.matplotSpectrogram(w, nameOfFiles)
    elif inp == 4:
        print("\nUsing Seaborn, here is the FFT: ")
        seaCustom.seaFFT(w, nameOfFiles)
    elif inp == 5:
        print("\nUsing Matplotlib, here is the contour graph of your wavelet: ")
        coeffs, freqs, sig, rate, sampPeriod, timeArray = waveletF.wavelets(w, nameOfFiles)
        waveletF.contourWavelet(coeffs, timeArray, freqs, nameOfFiles)
    elif inp == 6:
        print("\nUsing Plotly, here is the waveform: ")
        plotCustom.plotlyWaveform(w, nameOfFiles)
    elif inp == 7:
        print("\nUsing Bokeh, here is the FFT plots: ")
        bokeh.bokehFFT(w, nameOfFiles)
    else:
        print("invalid input!")
    


# %%
