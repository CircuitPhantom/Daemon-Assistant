# Daemon Assistant
Daemon Assistant is a terminal UI for running Ollama models with tools.


## Usage
- You need Ollama installed and running on your system before using Daemon Assistant
- Clone the repository with ``git clone https://github.com/CircuitPhantom/Daemon-Assistant.git``.
- Go to /Daemon-Assistant ``cd ./Daemon-Assistant``.
- Create a virtual environment it Python with ``python -m venv venv`` and activate with ``source venv/bin/activate``.  
  *(Optional, recommended for Linux systems)*
- Install Ollama library for Python ``pip install ollama``.
- Run the code with ``python main.py``, ``python test.py`` or ``python test2.py``.
- Type ``/help`` for more info.

**main.py** is the simplest version with no tool calling.  
**test.py** can call tools but can't chain them.  
**test2.py** is the most capable version and can chain tools.

## Tools
Tools are defined in **tools.py**.  
The only tool for now is ``execute_command`` that gives the model to execute commands on the system.   

**IMPORTANT:** Currently there is **no safety** for executing commands so be careful when using this tool!

## Commands
Commands are called from **commands.py**.    
Type ``/{command}`` to call a command.  

- ``/model`` lists models, use with ``-a`` flag for detailed list.
- ``/model {model name}`` switches models.
- ``/think`` toggles thinking.
- ``/pull {model name}`` pulls a model from Ollama.
- ``/remove {model name}`` deletes a model.
- ``/bye`` quit code
- ``/help`` prints help menu

## License

This repository is licensed under the **MIT License** — see [`LICENSE`](./LICENSE). Feel free to fork, remix, and make your own.
