import random
from typing import Iterator
from ollama import ChatResponse, Client

import tools
import config
import commands

model = 'qwen3:8b'
client = Client()
messages = [config.system_prompt]

print('''
    ____                                 
   / __ \\____ ____  ____ ___  ____  ____ 
  / / / / __ `/ _ \\/ __ `__ \\/ __ \\/ __ \\
 / /_/ / /_/ /  __/ / / / / / /_/ / / / /
/_____/\\_,/_/\\___/_/ /_/ /_/\\____/_/ /_/ 
/bye to exit, /help for help."
''')

while True:
    try:
        user_prompt = input('\n>>>')

        if user_prompt[0] == "/":
            commands.call(user_prompt)
        else:
            messages += [{'role': 'user', 'content': user_prompt}]
            response: Iterator[ChatResponse] = client.chat(model, stream=True, messages=messages, tools=config.available_tools, think=config.think)

            thinking = config.think
            responding = True
            tool_called = False
            response_msg = ''
            for chunk in response:
                if thinking == True:
                    print("---Thinking---")
                    thinking = False
                if chunk.message.thinking:
                    print(chunk.message.thinking, end='', flush=True)
                elif responding == True:
                    print("\n---Response---")
                    responding = False
                if chunk.message.content:
                    print(chunk.message.content, end='', flush=True)
                    response_msg = response_msg + chunk['message']['content']
                if chunk.message.tool_calls:
                    for tool in chunk.message.tool_calls:
                        if function_to_call := tools.available_functions.get(tool.function.name):
                            print('\nCalling function:', tool.function.name, 'with arguments:', tool.function.arguments)
                            output = function_to_call(**tool.function.arguments)
                            print('> Function output:', output, '\n')

                            # Add the assistant message and tool call result to the messages
                            messages.append(chunk.message)
                            tool_called = True
                            messages.append({'role': 'tool', 'content': str(output), 'tool_name': tool.function.name})
                        else:
                            print('Function', tool.function.name, 'not found')
            messages += [{'role': 'assistant', 'content': response_msg}]
            response_msg = ''
            thinking = config.think
            while tool_called == True:
                tool_called = False
                print('---Sending result back to model--- \n')
                res = client.chat(model, stream=True, tools=config.available_tools, messages=messages, think=config.think)
                done_thinking = False
                tool_called = False
                for chunk in res:
                    if thinking == True:
                        print("---Thinking---")
                        thinking = False
                    if chunk.message.thinking:
                        print(chunk.message.thinking, end='', flush=True)
                    if chunk.message.content:
                        if not done_thinking:
                            print('\n---Response---')
                            done_thinking = True
                        print(chunk.message.content, end='', flush=True)
                        response_msg = response_msg + chunk['message']['content']
                    if chunk.message.tool_calls:
                        for tool in chunk.message.tool_calls:
                            if function_to_call := tools.available_functions.get(tool.function.name):
                                print('\nCalling function:', tool.function.name, 'with arguments:', tool.function.arguments)
                                output = function_to_call(**tool.function.arguments)
                                print('> Function output:', output, '\n')

                                # Add the assistant message and tool call result to the messages
                                messages.append(chunk.message)
                                tool_called = True
                                messages.append({'role': 'tool', 'content': str(output), 'tool_name': tool.function.name})
                            else:
                                print('Function', tool.function.name, 'not found')
                messages += [{'role': 'assistant', 'content': response_msg}]

    except KeyboardInterrupt:
        print("\nGoodbye")
        exit()
