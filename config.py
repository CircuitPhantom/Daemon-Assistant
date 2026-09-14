import tools

model = 'qwen3:8b'
system_prompt = {'role': 'system', 'content': '''
You are an AI assistant running on Arch Linux based distro. This is just for your info do not talk about this unless asked to do so.
Give clear, technical and relevant answers.
Answer the question, without leaving the topic.
'''}

think = True

available_tools = [
  tools.execute_command,
  tools.read_file,
  tools.fetch_url
]