from ollama import ListResponse, list
import ollama
import config

#Call commands
def call(msg):
    if msg == '/model':
        listLLM()

    elif msg == '/model -a':
        listLLM_adv()

    elif msg[:6] == '/model':
        lm(msg)

    elif msg == '/think': #Toggle Thinking
        if config.think == True:
            config.think = False
            print("Thinking: OFF")
        else:
            config.think = True
            print("Thinking: ON")

    elif msg[:5] == '/pull':
        try:
            ollama.pull(msg[6:])
        except ollama._types.ResponseError:
            print("Couldn't find model", msg[6:])

    elif msg[:7] == '/remove':
        try:
            ollama.delete(msg[8:])
        except ollama._types.ResponseError:
            print("Couldn't find model", msg[8:])

    elif msg == '/bye':
        print("Goodbye")
        exit()

    elif msg == '/help':
        print('''
Usage:
    Pull an Ollama model if you haven't done yet (See "Commands" to install now or install from your terminal with "ollama pull {model name}").
    After that, relaunch and just type your prompt and hit enter to send; model will start generating response.
    /bye or Ctrl+C to exit

Commands:
    Usage: Type "/{command}" and hit enter to use a command.

    /model - List installed models.
    /model {model name} - Switch model.
    /think - Toggle thinking in supported models.
    /pull {model name} - Pull (install) a model.
    /remove {model name} - Remove (uninstall) a model.
    /bye - Quit.
''')
    else:
        print('Invalid command.\nType "/help" for commands')


#--------------------------------------------------------------------------------------------------------------------------#
#List models
def listLLM():
    response: ListResponse = list()

    print("Models:")
    for model in response.models:
        print('-', model.model)
    print('\nType "/model -a" for detailed view,\n"/model {model name}" to switch models')

#List details
def listLLM_adv():
    response: ListResponse = list()

    print("Models:")
    for model in response.models:
        print('-', model.model)
        print('   |— Size (MB):', f'{(model.size.real / 1024 / 1024):.2f}')
        if model.details:
            print('   |— Family:', model.details.family)
            print('   |— Parameter Size:', model.details.parameter_size)
            print('   |— Quantization Level:', model.details.quantization_level)
        print("\n")
    print('Type "/model {model name}" to switch models')

#Choose model
def lm(x):
    x = x[7:]
    arr=[]

    response: ListResponse = list()
    for model in response.models:
        arr.append(model.model)
    if x in arr:
        config.model=x
        print("Choosen model:", x)
    else:
        print('Invalid model name.\nType "/models" for available models')
