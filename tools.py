import random

def get_temperature(city: str) -> int:
  """
  Get the temperature for a city in Celsius

  Args:
    city (str): The name of the city

  Returns:
    int: The current temperature in Celsius
  """
  # This is a mock implementation - would need to use a real weather API
  import random

  if city not in ['London', 'Paris', 'New York', 'Tokyo', 'Sydney']:
    return 'Unknown city'

  return str(random.randint(0, 35)) + ' degrees Celsius'

def get_conditions(city: str) -> str:
  """
  Get the weather conditions for a city
  """
  if city not in ['London', 'Paris', 'New York', 'Tokyo', 'Sydney']:
    return 'Unknown city'
  # This is a mock implementation - would need to use a real weather API
  conditions = ['sunny', 'cloudy', 'rainy', 'snowy']
  return random.choice(conditions)

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
  'get_temperature': get_temperature,
  'get_conditions': get_conditions,
  'execute_command': execute_command
}

available_tools = [
    get_temperature,
    get_conditions,
    execute_command
]