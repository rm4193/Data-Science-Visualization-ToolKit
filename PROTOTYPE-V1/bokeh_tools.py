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
from pydub import AudioSegment # immutable objects
import mpld3
from scipy import stats
import wavio
from bokeh.io import show, output_notebook
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
import holoviews as hv #There is a reason we have to do this here but its not important. Holoviews is the next library
hv.extension('bokeh')

import tkinter as tk
from tkinter import filedialog

# custom module below
from Fourier import Fourier
import FourierAnalysisTools as ft

#%%
def bokehFFT(w, nameOfFiles):
    freqArray, fftp = ft.fftMultipleFiles(w)
    #arrayOfFigs = ft.arrayOfPlotly(nameOfFiles, freqArray, fftp)

    for i in range(len(fftp)):
        p = figure(title = nameOfFiles[i], plot_width = 800, plot_height = 800)
        intenVal = 10*log10(fftp[i])
        p.line(x = freqArray[i], y = intenVal)
        p.xaxis[0].axis_label = 'Time' # change x-axis label
        p.yaxis[0].axis_label = 'Frequency' # change y-axis label
        show(p)


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





