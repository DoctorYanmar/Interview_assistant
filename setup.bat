@echo off
setlocal enabledelayedexpansion

:: Set UTF-8 encoding
chcp 65001 > nul

:: Change to the script's directory
cd /d "%~dp0"

:: Check for necessary folders
if not exist "portable_python" mkdir portable_python
if not exist "venv" mkdir venv

:: Download portable Python if it doesn't exist
if not exist "portable_python\python.exe" (
    echo Downloading portable Python...
    curl -L "https://www.python.org/ftp/python/3.10.11/python-3.10.11-embed-amd64.zip" -o python.zip
    if %errorlevel% neq 0 (
        echo Error downloading Python. Check your internet connection and try again.
        pause
        exit /b 1
    )
    
    echo Extracting Python...
    tar -xf python.zip -C portable_python
    if %errorlevel% neq 0 (
        echo Error extracting Python. Please install tar or extract the zip file manually.
        pause
        exit /b 1
    )
    del python.zip
)

:: Verify Python installation
if not exist "portable_python\python.exe" (
    echo Error: python.exe not found in the portable_python folder.
    echo Please extract the Python zip file manually to the portable_python folder.
    pause
    exit /b 1
)

:: Modify python310._pth file
echo python310.zip> portable_python\python310._pth
echo .>> portable_python\python310._pth
echo import site>> portable_python\python310._pth

:: Download get-pip.py if it doesn't exist
if not exist "get-pip.py" (
    echo Downloading get-pip.py...
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
)

:: Install pip
portable_python\python.exe get-pip.py

:: Add Scripts to PATH temporarily
set PATH=%cd%\portable_python;%cd%\portable_python\Scripts;%PATH%

:: Install virtualenv
portable_python\python.exe -m pip install virtualenv

:: Create virtual environment using virtualenv
echo Creating virtual environment...
portable_python\python.exe -m virtualenv venv
if %errorlevel% neq 0 (
    echo Error creating virtual environment.
    pause
    exit /b 1
)

:: Activate virtual environment
call venv\Scripts\activate.bat

:: Upgrade pip in virtual environment
python -m pip install --upgrade pip

:: Check for requirements.txt
if not exist "requirements.txt" (
    echo Error: requirements.txt file not found in the current directory.
    echo Current directory: %CD%
    echo Contents of current directory:
    dir
    pause
    exit /b 1
)

:: Install dependencies
pip install -r requirements.txt

:: Verify installation of key packages
python -c "import dotenv; import openai; import numpy; import sounddevice; import PyQt6" || (
    echo Error: Some required packages are not installed correctly.
    echo Please check your internet connection and try running setup.bat again.
    pause
    exit /b 1
)

:: Create .env file if it doesn't exist
if not exist ".env" (
    echo OPENAI_API_KEY=your_api_key_here > .env
)

start "" "https://vb-audio.com/Cable/"

echo Installation complete. Please download and install VB-Audio Virtual Cable from https://vb-audio.com/Cable/
echo Then edit the .env file to add your OpenAI API key.
echo To run the program, use interview_assistant.bat
pause