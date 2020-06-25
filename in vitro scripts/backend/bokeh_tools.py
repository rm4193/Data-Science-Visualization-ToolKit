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
from scipy import stats
#import wavio
from bokeh.io import show, output_notebook, export_png
from bokeh.models import (
    ColumnDataSource,
    HoverTool,
    LinearColorMapper,
    BasicTicker,
    PrintfTickFormatter,
    ColorBar,
    FactorRange
)
from bokeh.plotting import figure, show, output_notebook
from bokeh.palettes import BuPu
#import holoviews as hv #There is a reason we have to do this here but its not important. Holoviews is the next library
#hv.extension('bokeh')

import tkinter as tk
from tkinter import filedialog

# custom module below
from backend.Fourier import Fourier
import backend.FourierAnalysisTools as ft

#%%
def find_nearest( array, value  ):
    array = np.asarray(array)
    idx = ( np.abs( array - value)).argmin()
    return idx


#%%
def bokehFFT(w, nameOfFiles):
    root = tk.Tk()
    dirname = filedialog.askdirectory(title='Please select a directory to save your bokeh FFT graphs')

    freqArray, fftp = ft.fftMultipleFiles(w)
    #arrayOfFigs = ft.arrayOfPlotly(nameOfFiles, freqArray, fftp)
    root.destroy()

    minfreq=20 # change the number to whatever minimum frequency you want to see
    maxfreq=3000 # change the number to whatever maximum frequency you want to see

    for i in range(len(fftp)):
        p = figure(title = nameOfFiles[i], plot_width = 800, plot_height = 800)
        intenVal = 10*log10(fftp[i])

        minfreqIndex = find_nearest( freqArray[i], minfreq   ) 
        maxfreqIndex = find_nearest( freqArray[i], maxfreq ) 

        freqRange = freqArray[i][minfreqIndex:maxfreqIndex+1]
        intenVal = intenVal[minfreqIndex:maxfreqIndex+1]

        p.line(x = freqRange, y = intenVal)
        p.xaxis[0].axis_label = 'Frequency' # change x-axis label
        p.yaxis[0].axis_label = 'Intensity' # change y-axis label
        export_png(p, filename=dirname+'/'+nameOfFiles[i]+'_bokeh_FFT'+'.png')
        #show(p)


#%% SPECTROGRAM
'''
def bokehSpect(w, nameOfFiles):
    freqArray, fftp = ft.fftMultipleFiles(w)

    for i in range(len(fftp)):

        intenVal = 10*log10(fftp[i])
        timeLen = arange(0, w[i].data.shape[0], 1)
        timeLen = timeLen/w[i].rate
        timeLen = timeLen[:len(intenVal)]

        # Bokeh doesn't have its own gradient color maps supported but you can easily use on from matplotlib.
        colormap =cm.get_cmap("BuPu")
        bokehpalette = [mpl.colors.rgb2hex(m) for m in colormap(np.arange(colormap.N))]
        
        #this mapper is what transposes a numerical value to a color. 
        mapper = LinearColorMapper(palette=bokehpalette, low=min(intenVal), high=max(intenVal))
        colors = {'field': intenVal, 'transform': mapper}
        #color_bar = ColorBar( color_mapper=mapper, location=( 0, 0))

        timeLen = list(timeLen.astype('str'))
        freqArray[i] = list(freqArray[i].astype('str'))

        data = {
            'x_values': timeLen,
            'y_values': freqArray[i],
            'z_values': intenVal
        }

        #ColumnDataSource is bokeh fancy shared datasource. Not applicable here but it would generally allow the sharing of one data source
        #with multiple charts.
        source = ColumnDataSource(data=data)

        z = figure(title="Heatmap", x_range=timeLen, y_range=freqArray[i])

        z.rect(x='x_values', y='y_values', width=1, height=1, source = source,
            fill_color={'field': 'z_values', 'transform': mapper},
            line_color=None)

        color_bar = ColorBar(color_mapper=mapper, major_label_text_font_size="5pt",
                            ticker=BasicTicker(desired_num_ticks=8),
                            formatter=PrintfTickFormatter(format="%d%%"),
                            label_standoff=6, border_line_color=None, location=(0, 0))
        z.add_layout(color_bar, 'right')
        z.xaxis.axis_label = 'Time (s)'
        z.yaxis.axis_label = 'Freq (Hz)'


        show(z)
'''





