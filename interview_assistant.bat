@echo off
setlocal enabledelayedexpansion

:: Change to the script's directory
cd /d "%~dp0"

:: Activate virtual environment
call venv\Scripts\activate.bat

pip install -r requirements.txt

:: Verify activation of virtual environment
python -c "import sys; print(sys.prefix)"

:: Set PATH to include portable Python and its Scripts folder
set PATH=%cd%\venv\Scripts;%cd%\portable_python;%cd%\portable_python\Scripts;%PATH%

:: Run the main script
python main.py

pause