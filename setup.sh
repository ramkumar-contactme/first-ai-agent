# Create a new virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
# source venv/bin/activate

# Install the required packages
python -m pip install --upgrade pip
pip install uagents

pip freeze > requirements.txt

# Start agents in separate terminals (Windows)
start cmd /k "venv\Scripts\activate && python slave-agent1.py"
start cmd /k "venv\Scripts\activate && python slave-agent2.py"
start cmd /k "venv\Scripts\activate && python master-agent.py"

# For Linux/macOS, use:
# gnome-terminal -- bash -c "source venv/bin/activate && python slave-agent1.py; exec bash"
# gnome-terminal -- bash -c "source venv/bin/activate && python slave-agent2.py; exec bash"
# gnome-terminal -- bash -c "source venv/bin/activate && python master-agent.py"
