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
import FourierAnalysisToolsForPackage as ft
import mainMultipleFFTs_matplot as matCustom
import mainMultipleFFTs_plotly as plotCustom
import mainMultipleFFTs_seaborn as seaCustom



#%% METHOD 1
options = ['plotly FFT', 'matplot FFT', 'matplot Spectrogram', 'seaborn FFT']
print("Select a number for the corresponding graph you want\n")
for i in range(len(options)):
    print(str(i+1) + ":", options[i]) 

inp = int(input("Enter a number: "))

if inp == 1:
    print("\nUsing Plotly, here is the FFT: ")
    plotCustom.plotlyFFT()
elif inp == 2:
    print("\nUsing Matplotlib, here is the FFT: ")
    matCustom.matplotFFT()
elif inp == 3:
    print("\nUsing Matplotlib, here is the spectrogram: ")
    matCustom.matplotSpectrogram()
elif inp == 4:
    print("\nUsing Seaborn, here is the FFT: ")
    seaCustom.seaFFT()
else:
    print("invalid input!")






#%% METHOD 2
#plotCustom.plotlyFFT()
#matCustom.matplotFFT()
#matCustom.matplotSpectrogram()
#seaCustom.seaFFT()






