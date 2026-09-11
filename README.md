# Daemon Assistant
Daemon Assistant is a terminal UI for running Ollama models with tools.


## Usage
- You need Ollama installed and running on your system before using Daemon Assistant
- Clone the repository with ``git clone https://github.com/CircuitPhantom/Daemon-Assistant.git``.
- Navigate into the folder with ``cd ./Daemon-Assistant``.
- Create a virtual environment in Python with ``python -m venv venv`` and activate with ``source venv/bin/activate``.  
  *(Optional, recommended for Linux systems)*
- Install the Ollama Python library ``pip install ollama``.
- Run the code with ``python main.py``, ``python test.py`` or ``python test2.py``.
- Type ``/help`` for more info.

**main.py** is the simplest version with no tool calling.  
**test.py** can call tools but can't chain them.  
**test2.py** is the most capable version and can chain tools.

## Tools
Tools are defined in **tools.py**.  
The only tool for now is ``execute_command`` that gives the model the ability to execute commands on the system.   

**IMPORTANT:** Currently there is **no safety** for executing commands so be careful when using this tool!

## Commands
Commands are called from **commands.py**.    
Type ``/{command}`` to call a command.  

- ``/model`` lists models, use with ``-a`` flag for detailed list.
- ``/model {model name}`` switches models.
- ``/think`` toggles thinking.
- ``/pull {model name}`` pulls a model from Ollama.
- ``/remove {model name}`` deletes a model.
- ``/bye`` quits the program.
- ``/help`` prints help menu.

## Model Licenses

Daemon Assistant runs models through Ollama. Ollama itself is licensed under
Apache 2.0, but the models you run through it (Llama, Mistral, etc.) carry
their own separate licenses — some of these, like Meta's Llama license,
include usage restrictions beyond what the MIT license on this repo allows.
Check the license of whichever model you pull before using it in production
or redistributing outputs.

## Disclaimer

This tool gives the model the ability to execute shell commands on your
system via ``execute_command``, with **no sandboxing or safety checks**. Use
it at your own risk, ideally in an isolated or disposable environment. This
software is provided "as is", without warranty of any kind (see LICENSE).

## License

This repository is licensed under the **MIT License** — see [`LICENSE`](./LICENSE). Feel free to fork, remix, and make your own.
