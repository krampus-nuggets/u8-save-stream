# Package Imports
import os
import yaml
from sys import platform
from colorama import Fore, Back, Style
from glob import glob
from typing import List

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

# HELPER - Check OS
def is_windows():
  if platform == "win32":
    return True
  
  return False

# HELPER - Get filename from files in directory by extension
def get_filenames(path: str, extension: str):
  glob_path = f"{path}\\*.{extension}" if is_windows() else f"{path}/*.{extension}"
  files = glob(glob_path)

  # Get only the base file
  result_files = list(map(lambda file: os.path.basename(file), files))
  # Strip extension from file
  result_files = list(map(lambda file: file.split(".")[0], result_files))

  return result_files

# HELPER - Get remainder files to be downloaded
def get_valid_streams(filenames: List, streams: List):
  try:
    # CHECK - Downloads not started yet
    if len(filenames) == 0:
      return streams

    unsaved_streams = []

    for file in filenames:
      for stream in streams:
        if file == stream["filename"]:
          unsaved_streams.append(stream)
    
    return unsaved_streams
  except Exception:
    return None
