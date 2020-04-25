@echo off

rem This is an installer of various packages automatically
rem call C:\Users\%USERNAME%\Anaconda3/Scripts/activate.bat <anaconda_dir>
rem call <anaconda_dir>/Scripts/activate.bat <anaconda_dir>

rem This is example of a comment >>C:\Users\%USERNAME%\Anaconda3

rem One method of doing installations:
rem 1) Download scipy package
rem still need to figure out how to put file in specific locations
rem echo "Downloading Anaconda"
rem powershell -Command "Invoke-WebRequest [web address] -Outfile [name of outfile]"
rem Anaconda prompt shell address: "C:\Users\BA_INTERN\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Anaconda3 (64-bit)\Anaconda Prompt (Anaconda3).lnk"



rem START OF BATCH FILE BELOW

rem First find where Anaconda prompt is to use pip
rem Then call Anaconda prompt
rem This was done by finding Anaconda Prompt location and searched its path in properties
call %HOMEDRIVE%\Users\%USERNAME%\Anaconda3\Scripts\activate.bat %HOMEDRIVE%\Users\%USERNAME%\Anaconda3

rem use pip to install various packages
pip install wavio
pip install tkinter
pip install pywt
pip install scaleogram


cls
@echo All extra packages have been installed!
@echo Press enter to exit
pause





