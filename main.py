#%% IMPORTING PACKAGES (click shift+enter to run cell)

from Fourier import Fourier
import FourierAnalysisTools as ft
import matplotlibCustom as matCustom
import plotlyCustom as plotCustom
import seabornCustom as seaCustom
import waveletFunction as waveletF
import bokeh_tools as bokeh
import altairCustom as altairM

print("All packages have been imported successfully!")


#%% Choose files and name the files (click shift+enter to run cell)
w, nameOfFiles = ft.fileLoading() # creates an array of files and array of names for each file
print("All WAV files have been imported successfully!")


#%% Visualization tool choice section (click shift+enter to run cell)
options = ['Plotly FFT', 'Matplot FFT', 'Matplot Spectrogram', 'Seaborn FFT', 'Matplotlib contour plot of wavelet', 'Plotly Waveform', 'Bokeh FFT', 'Altair waveform', 'Altair FFT']
print("The list of the different types of graphs:")
print("\n")
for j in range(len(options)):
    print(options[j])

num = int(input("Please type the number of graphs styles that are required. The options are shown below."))

for j in range(num):
    print("\nThe list of the different types of graphs:")
    for i in range(len(options)):
        print(str(i+1) + ":", options[i]) 

    inp = int(input("Select a number for the corresponding graph you want. The options are shown below."))

    if inp == 1:
        print("\nUsing Plotly, here is the FFT: ")
        plotCustom.plotlyFFT(w, nameOfFiles)
    elif inp == 2:
        print("\nYour Matplotlib FFT plots are saved in the file directory of your choice")
        print("\nUsing Matplotlib, here is the FFT: ")
        matCustom.matplotFFT(w, nameOfFiles)
    elif inp == 3:
        print("\nYour Matplotlib spectrogram plots are saved in the file directory of your choice")
        print("\nUsing Matplotlib, here is the spectrogram: ")
        matCustom.matplotSpectrogram(w, nameOfFiles)
    elif inp == 4:
        print("\nUsing Seaborn, here is the FFT: ")
        seaCustom.seaFFT(w, nameOfFiles)
    elif inp == 5:
        print("\nYour Matplotlib wavelet contour plots are saved in the file directory of your choice")
        coeffs, freqs, sig, rate, sampPeriod, timeArray = waveletF.wavelets(w, nameOfFiles)
        matCustom.contourWavelet(coeffs, timeArray, freqs, nameOfFiles)
    elif inp == 6:
        print("\nUsing Plotly, here is the waveform: ")
        plotCustom.plotlyWaveform(w, nameOfFiles)
    elif inp == 7:
        print("\nYour Bokeh FFT plots are saved in the file directory of your choice")
        bokeh.bokehFFT(w, nameOfFiles)
    elif inp == 8:
        print("\nUsing Altair, here is your waveform:")
        altairM.altairWaveform(w, nameOfFiles)
    elif inp == 9:
        print("\nUsing Altair, here is your FFT:")
        altairM.altairFFT(w, nameOfFiles)
    else:
        print("invalid input!")
    

# %%
from distributed import Client
client = Client()

# %%
