#!/bin/bash

# Create a new virtual environment
python -m venv venv

# Activate the virtual environment
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    source venv/Scripts/activate  # Windows
else
    source venv/bin/activate  # macOS/Linux
fi

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install uagents

# Save dependencies to requirements.txt
pip freeze > requirements.txt

# Navigate to the agents directory
cd first-ai-agent/agents || exit

# Run agents in separate terminals (Windows & Linux/macOS compatible)
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    start cmd /k "venv\Scripts\activate && python agent1.py"
    start cmd /k "venv\Scripts\activate && python agent2.py"
    start cmd /k "venv\Scripts\activate && python communicate.py"
else
    gnome-terminal -- bash -c "source venv/bin/activate && python agent1.py; exec bash" &
    gnome-terminal -- bash -c "source venv/bin/activate && python agent2.py; exec bash" &
    gnome-terminal -- bash -c "source venv/bin/activate && python communicate.py; exec bash" &
fi

echo "Agents started successfully!"
