# Package Imports
import os
import yaml
from colorama import Fore, Back, Style

# Internal Imports


# CHECK - File Exists
def check_config(config_uri: str):
  check = os.path.isfile(config_uri)
  return check

# HELPER - Read Config File
def read_config(config_uri: str):
  try:
    stream = open(config_uri, "r")
    return yaml.load(stream, Loader=yaml.SafeLoader)
  except Exception:
    return None

# HELPER - Terminal Output
def term_output(type: str, value: str):
  is_string = isinstance(value, str)

  # ERROR
  if (type == "error"):
    print(Back.RED + Fore.BLACK + "ERROR:")

  # INFO
  if (type == "info"):
    print(Back.WHITE + Fore.BLACK + "INFO:")
  
  # SUCCESS
  if (type == "success"):
    print(Back.GREEN + Fore.BLACK + "SUCCESS:")

  # NON-STRING VALUE
  if (not is_string):
    print(Style.RESET_ALL)
    print(value)
    return

  print(Style.RESET_ALL + value)
