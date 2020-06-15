from pylab import*
from scipy.io import wavfile
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
import pandas as pd
from scipy import stats
import wavio
import seaborn as sns

import tkinter as tk
from tkinter import filedialog

import glob
import os

# add this package to the installation batch script
# https://pypi.org/project/pyloudnorm/
# pip install pyloudnorm
# pip install soundfile

import pyloudnorm as pyln
import soundfile as sf


#%%
def listOfAudioFiles():
    root = tk.Tk()
    dirname = filedialog.askdirectory(title='Please select a directory of WAV files you want to analyze')
    newDirName = os.path.normpath(dirname) # converts tkinter directory path to normal OS path labeling
    w = list(glob.glob(os.path.join(newDirName, '*.wav')))
    nameOfFiles = [None]*len(w)
    rate = [None]*len(w)
    root.destroy()

    #renaming the files brute force
    for i in range(len(w)):
        lastChar_index = w[i].rfind("\\") # finds the index of the last occurrence of the input value - need to change per OS
        temp = w[i][lastChar_index+1:]
        secChar_index = temp.rfind(".")
        realName = temp[:secChar_index]
        nameOfFiles[i] = realName
        #res = re.findall(r'\w')
        #res = re.search('(.WAV|.wav)', fname) # looks for upper or lowercase .wav files
    
    for i in range(len(w)):
        w[i], rate[i] = sf.read(w[i])
    
    return w, rate, nameOfFiles

#%%
def pairUp(internalPinkWav, internalPinkRate, internalPinkName, externalPinkWav, externalPinkRate, externalPinkName):
    
    cols = ['Stethoscope and day number', 'Pink Internal LUFS (dB)', 'Pink External LUFS (dB)', 'Delta LUFS']
    df = pd.DataFrame(columns = cols)
    substring = '_'
    for i in range(len(internalPinkName)):
        string1 = internalPinkName[i]
        index1 = string1.find(substring)
        string1 = string1[index1+1:]
        
        for j in range(len(externalPinkName)):
            string2 = externalPinkName[j]
            index2 = string2.find(substring)
            string2 = string2[index2+1:]
            
            if string1 == string2:
                
                meter1 = pyln.Meter(internalPinkRate[i]) # create BS.1770-4 meter
                loudness1 = meter1.integrated_loudness(internalPinkWav[i]) # measure loudness
                #loudness1 = round(loudness1,4)
    
                meter2 = pyln.Meter(externalPinkRate[j]) # create BS.1770-4 meter
                loudness2 = meter2.integrated_loudness(externalPinkWav[j]) # measure loudness
                #loudness2 = round(loudness2,4)
                
                # external pink noise lufs - internal pink noise lufs
                delta = loudness2-loudness1
                
                df = df.append({'Stethoscope and day number': string1,  'Pink Internal LUFS (dB)':loudness1,
                                'Pink External LUFS (dB)':loudness2, 'Delta LUFS':delta  }, ignore_index=True)
                
    root = tk.Tk()
    dirname = filedialog.askdirectory(title='Please select a directory to save your LUFS chart')            
    df.to_csv(dirname+'/'+'LUFS chart.csv')
    root.destroy()
    
    return df

