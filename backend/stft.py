#%%
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
import math

import tkinter as tk
from tkinter import filedialog

# custom module below
from backend.Fourier import Fourier
import backend.FourierAnalysisTools as ft 

#%%
def stftCustom( w1, nameOfFiles ):

    for i in range(len(w1)):
        timeArray1 = ft.timeList(w1[i])
        #%% Short time Fourier Transform (STFT) over the file
        w1_chunks1 = ft.chunkIt(w1[i], timeArray1, 4)
        freqArray1, fftp1 = ft.scanningFFTOneFile(w1_chunks1, w1[i].rate)

        #%% Plotting STFT over ONE file
        fig1 = go.Figure()

        for i in range(len(fftp1)):
            fig1.add_trace(go.Scatter(
                x = freqArray1[i],
                y = 10*np.log10(fftp1[i])
            ))

        fig1.update_layout(
            title="HOCM-01 Rolling FFT - aortic auscultation with MDPS",
        )

        fig1.update_xaxes(title_text='Frequency (Hz)')
        fig1.update_yaxes(title_text='Intensity (dB)')
        fig1.show()

# %%
