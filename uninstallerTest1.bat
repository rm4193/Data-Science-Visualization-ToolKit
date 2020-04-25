@echo off

rem This is a test uninstaller of specific python packages

call %HOMEDRIVE%\Users\%USERNAME%\Anaconda3\Scripts\activate.bat %HOMEDRIVE%\Users\%USERNAME%\Anaconda3

rem use pip to uninstall various packages
pip uninstall scipy
pip uninstall pandas
pip uninstall numpy
pip uninstall matplotlib
pip uninstall plotly
pip uninstall wavio
pip uninstall tkinter
pip uninstall bokeh
pip uninstall pywt
pip uninstall scaleogram
pip uninstall seaborn


cls
pause