@echo off

rem This is a test uninstaller of specific python packages

call %HOMEDRIVE%\Users\%USERNAME%\Anaconda3\Scripts\activate.bat %HOMEDRIVE%\Users\%USERNAME%\Anaconda3

rem use pip to uninstall various packages
pip uninstall plotly
pip uninstall wavio
pip uninstall tkinter
pip uninstall pywt
pip uninstall scaleogram
pip uninstall altair
pip uninstall altair_viewer
pip uninstall altair_saver
pip uninstall selenium
pip uninstall modin[all]
pip uninstall glob
pip uninstall pyloudnorm
pip uninstall soundfile
pip uninstall pillow


cls
@echo All extra packages have been uninstalled!
@echo Press enter to exit
pause
