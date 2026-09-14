
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

def read_file(file):
  """
  Read contents of a file

  Args:
    file: File to read

  Returns:
    output: File contents
  """

  with open(file) as f:
    output = f.read()

  return output

def fetch_url(url):
  """
  Fetch website from an URL
  
  Args:
    url: URL to fetch, must be full (https://...)
    
  Returns:
    response: Response from URL
  """

  import requests

  response = requests.get(url)
  if response.ok:
    return response.text
  else:
    response_err = f"Error Code:{response.status_code}\n{response.text}"
    return response_err


available_functions = {
  'execute_command': execute_command,
  'read_file': read_file,
  'fetch_url': fetch_url
}