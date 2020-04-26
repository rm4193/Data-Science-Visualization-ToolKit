@echo off

rem This is a test uninstaller of specific python packages

call %HOMEDRIVE%\Users\%USERNAME%\Anaconda3\Scripts\activate.bat %HOMEDRIVE%\Users\%USERNAME%\Anaconda3

rem use pip to uninstall various packages
pip uninstall plotly
pip uninstall wavio
pip uninstall tkinter
pip uninstall pywt
pip uninstall scaleogram


cls
@echo All extra packages have been uninstalled!
@echo Press enter to exit
pause
