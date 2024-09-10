#!/bin/bash

set -e

# Change to the script's directory
cd "$(dirname "$0")"

# Check for necessary folders
mkdir -p portable_python venv

# Download portable Python if it doesn't exist
if [ ! -f "portable_python/bin/python3" ]; then
    echo "Downloading portable Python..."
    curl -L "https://www.python.org/ftp/python/3.10.11/python-3.10.11-macosx10.9.pkg" -o python.pkg
    
    echo "Extracting Python..."
    xar -xf python.pkg
    cat Python_Framework.pkg/Payload | gunzip -dc | cpio -i
    mv Python.framework portable_python/
    rm -rf python.pkg Python_Framework.pkg
fi

# Verify Python installation
if [ ! -f "portable_python/Python.framework/Versions/Current/bin/python3" ]; then
    echo "Error: python3 not found in the portable_python folder."
    exit 1
fi

# Create symlink for easy access
ln -sf portable_python/Python.framework/Versions/Current/bin/python3 portable_python/python3

# Install pip
portable_python/python3 -m ensurepip

# Create virtual environment
echo "Creating virtual environment..."
portable_python/python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip in virtual environment
pip install --upgrade pip

# Check for requirements.txt
if [ ! -f "requirements.txt" ]; then
    echo "Error: requirements.txt file not found in the current directory."
    echo "Current directory: $(pwd)"
    echo "Contents of current directory:"
    ls -la
    exit 1
fi

# Install dependencies
pip install -r requirements.txt

# Verify installation of key packages
python -c "import dotenv; import openai; import numpy; import sounddevice; import PyQt6" || {
    echo "Error: Some required packages are not installed correctly."
    echo "Please check your internet connection and try running setup_macos.sh again."
    exit 1
}

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "OPENAI_API_KEY=your_api_key_here" > .env
fi

# Open VB-Audio Cable website
open "https://vb-audio.com/Cable/"

echo "Installation complete. Please download and install VB-Audio Virtual Cable from https://vb-audio.com/Cable/"
echo "Then edit the .env file to add your OpenAI API key."
echo "To run the program, use interview_assistant.sh"