# Daemon Assistant
Daemon Assistant is a terminal UI for running Ollama models with tools.


## Usage
- You need Ollama installed and running on your system before using Daemon Assistant
- Clone the repository with ``git clone https://github.com/CircuitPhantom/Daemon-Assistant.git``.
- Navigate into the folder with ``cd ./Daemon-Assistant``.
- Create a virtual environment in Python with ``python -m venv venv`` and activate with ``source venv/bin/activate``.  
  *(Optional, recommended for Linux systems)*
- Install required Python libraries ``pip install -r requirements``.
- Run the code with ``python main.py``.
- Type ``/help`` for more info.

## Tools
Tools are defined in **tools.py**.  
- ``execute_command`` gives the model the ability to execute commands on the system.   
- ``read_file`` lets the model read files without running command.  
- ``fetch_url`` to fetch web pages.  

**IMPORTANT:** Currently there is **no safety check** for executing commands so be careful when using ``execute_command``!  

**Known Issue:** Model might start explaining the HTML code after fetching an URL, this is not a bug. It happens when the HTML is too long and model's context window gets full.

## Commands
Commands are called from **commands.py**.    
Type ``/{command}`` to call a command.  

- ``/model`` lists models, use with ``-a`` flag for detailed list.
- ``/model {model name}`` switches models.
- ``/think`` toggles thinking.
- ``/pull {model name}`` pulls a model from Ollama.
- ``/remove {model name}`` deletes a model.
- ``/tools`` Turn on/off specific tools.
- ``/bye`` quits the program.
- ``/help`` for help menu.

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
