from ollama import chat
import ollama
import time

import commands
import config

messages=[]
messages.append(config.system_prompt)

print("Daemon AI\n/bye to exit, /help for help.\n")

try:
    while True:
        user_input = input(">>>")
        
        if user_input[0] == "/":
            commands.call(user_input)
        else:
            stream = chat(
                model=config.model,
                messages=messages + [{'role': 'user', 'content': user_input}],
                stream=True,
                think=config.think
            )

            response=''
            if config.think == True:
                print("Thinking:")
            try:
                for chunk in stream:
                    try:
                        print(chunk['message']['thinking'], end='', flush=True)
                    except KeyError:
                        print("\nResponse:")
                        print(chunk['message']['content'], end='', flush=True)
                        break
            except ollama._types.ResponseError:
                print("This model does not support thinking.")
                print("Thinking: OFF")
                config.think = False
                print("Please try again.")

            for chunk in stream:
                print(chunk['message']['content'], end='', flush=True)
                response = response + chunk['message']['content']
                
            messages += [
                {'role': 'assistant', 'content': response},
                {'role': 'user', 'content': user_input}]
            print('\n')

except KeyboardInterrupt:
    print("\nGoodbye")