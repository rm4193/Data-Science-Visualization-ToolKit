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
from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import ShortTermFeatures

import tkinter as tk
from tkinter import filedialog

# custom module below
from Fourier import Fourier
import FourierAnalysisTools as ft

#%%
w = ft.fileLoading()
Fs_array = []
x_array = []
F_array = [0]*len(w)
f_names_array = [0]*len(w)

#%%
for i in range(len(w)):
    Fs_array.append(w[i].rate)
    x_array.append(w[i].data[:,0])
    F_array[i], f_names_array[i] = ShortTermFeatures.feature_extraction(x_array[i], Fs_array[i], 0.050*Fs_array[i], 0.025*Fs_array[i])

#%%
plt.subplot(2,1,1); plt.plot(F_array[0][9,:]); plt.xlabel('Frame no'); plt.ylabel(f_names_array[0][9]) 
plt.subplot(2,1,2); plt.plot(F_array[0][10,:]); plt.xlabel('Frame no'); plt.ylabel(f_names_array[0][10]); plt.show()

plt.subplot(2,1,1); plt.plot(F_array[2][9,:]); plt.xlabel('Frame no'); plt.ylabel(f_names_array[2][9]) 
plt.subplot(2,1,2); plt.plot(F_array[2][10,:]); plt.xlabel('Frame no'); plt.ylabel(f_names_array[2][10]); plt.show()

# %%
plt.subplot(2,1,1); plt.plot(F_array[1][9,:]); plt.xlabel('Frame no'); plt.ylabel(f_names_array[1][9]) 
plt.subplot(2,1,2); plt.plot(F_array[1][10,:]); plt.xlabel('Frame no'); plt.ylabel(f_names_array[1][10]); plt.show()

plt.subplot(2,1,1); plt.plot(F_array[3][9,:]); plt.xlabel('Frame no'); plt.ylabel(f_names_array[3][9]) 
plt.subplot(2,1,2); plt.plot(F_array[3][10,:]); plt.xlabel('Frame no'); plt.ylabel(f_names_array[3][10]); plt.show()

# %%
