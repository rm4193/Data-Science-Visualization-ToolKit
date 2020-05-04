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
#import wavio
import seaborn as sns
import pywt
import scaleogram as scale
import gc

import tkinter as tk
from tkinter import filedialog

# custom module below
from Fourier import Fourier
import FourierAnalysisTools as ft

#%%
def wavelets(w, nameOfFiles):
    print("Please wait a moment to be directed for next steps")
    sig = []
    rate = []
    sampPeriod = []
    timeArray = []
    coeffs = []
    freqs = []

    for i in range(len(w)):
        sig.append(w[i].data[:,0])
        rate.append(w[i].rate)
        sampPeriod.append(1/rate[i])
        timeArray.append(ft.timeList(w[i]))

    # Wavelet calculation
    minScaleLimit = 80
    maxScaleLimit = 2000
    widths = np.arange(minScaleLimit, maxScaleLimit)
    # widths = np.arange(10, 1000)
    for i in range(len(w)):
        tempCoeffs, tempFreqs = scale.fastcwt(sig[i], widths, 'morl', sampling_period=sampPeriod[i])
        coeffs.append(tempCoeffs)
        freqs.append(tempFreqs)
        # converting scale coefficents to frequency: 
        #pywt.scale2frequency('morl', widths) / (sampPeriod)
        #normalCoeffs = coeffs
        #coeffs[:,0] = freqs

    return coeffs, freqs, sig, rate, sampPeriod, timeArray


def contourWavelet(coeffs, timeArray, freqs, nameOfFiles):
    root = tk.Tk()
    dirname = filedialog.askdirectory(title='Please select a directory to save your matplotlib wavelet contour plots')
    power = []
    normalizedCoeffs = []
    normalizedPower = []
    for i in range(len(coeffs)):
        power.append((abs(coeffs[i])) ** 2) # used to show just the positive wavelets
        normalizedCoeffs.append(coeffs[i]/np.abs(coeffs[i]).max()) # normalization factor of the coefficients
        normalizedPower.append(power[i]/np.abs(power[i]).max())
    for i in range(len(coeffs)):
        #plt.contourf(timeArray[i], freqs[i], normalizedPower[i], cmap='hot')
        plt.contourf(timeArray[i], freqs[i], normalizedCoeffs[i], cmap='hot')
        #plt.contourf(timeArray[i], freqs[i], coeffs[i], cmap='hot')
        #plt.contourf(timeArray[i], freqs[i], power[i], cmap='hot')
        
        plt.colorbar()
        plt.title(nameOfFiles[i])
        #plt.xlabel(str(input("Enter x axis name for contour plot: "))) 
        plt.xlabel("Time (ms)") # change x-axis label
        #plt.ylabel(str(input("Enter y axis name for contour plot: "))) 
        plt.ylabel("Frequency (Hz)") # change y-axis label
        plt.savefig(dirname+'/'+nameOfFiles[i]+'_wavelet_contour'+'.png')
        plt.close(fig=None)
        #gc.collect()
        #plt.yscale('log')


def heatMapWavelet(coeffs, nameOfFiles):
    power = []
    normalizedCoeffs = []
    normalizedPower = []
    for i in range(len(coeffs)):
        power.append((abs(coeffs[i])) ** 2)
        normalizedCoeffs.append(coeffs[i]/np.abs(coeffs[i]).max()) # normalization factor of the coefficients
        normalizedPower.append(power[i]/np.abs(power[i]).max())
    # Heat map of wavelet
    # you can delete or change cmap variable    
    for i in range(len(coeffs)):
        #plt.imshow(normalizedPower[i], cmap='hot', aspect='auto', vmax=abs(normalizedPower[i]).max(), vmin=-abs(normalizedPower[i]).max())
        plt.imshow(normalizedCoeffs[i], cmap='hot', aspect='auto', vmax=abs(normalizedCoeffs[i]).max(), vmin=-abs(normalizedCoeffs[i]).max())
        #plt.imshow(coeffs[i], cmap='hot', aspect='auto', vmax=abs(coeffs[i]).max(), vmin=-abs(coeffs[i]).max())
        #plt.imshow(power[i], cmap='hot', aspect='auto', vmax=abs(power[i]).max(), vmin=-abs(power[i]).max())
        
        plt.colorbar()
        plt.title(nameOfFiles[i])
        #plt.xlabel(str(input("Enter x axis name for contour plot: ")))
        plt.xlabel("Time (ms)") # change x-axis label
        #plt.ylabel(str(input("Enter y axis name for contour plot: ")))
        plt.ylabel("Frequency (Hz)") # change y-axis label
        plt.show()


    
    


# %%
