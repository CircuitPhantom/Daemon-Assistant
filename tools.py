
def execute_command(cmnd):
  """
  Execute a command on the host system

  Args:
    cmnd: Command to execute

  Returns:
    output: Command's output
  """

  import os
  output = os.popen(cmnd).read()

  return output


available_functions = {
  'execute_command': execute_command
}

available_tools = [
    execute_command
]