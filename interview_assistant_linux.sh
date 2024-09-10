#!/bin/bash

# Change to the script's directory
cd "$(dirname "$0")"

# Activate virtual environment
source venv/bin/activate

pip install -r requirements.txt

# Verify activation of virtual environment
python -c "import sys; print(sys.prefix)"

# Set PATH to include portable Python and its bin folder
export PATH="$(pwd)/portable_python/bin:$(pwd)/venv/bin:$PATH"

# Run the main script
python main.py